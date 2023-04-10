import os
import grpc
from concurrent import futures
from enum import Enum
from typing import Optional, Dict
from app.controllers import create_queue
from app.protos import messages_pb2_grpc, messages_pb2
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


class MessagesServicer(messages_pb2_grpc.MessagesServicer):

    def handle_grpc_request_from_gateway(self, request, context):
        with grpc.insecure_channel(f"{HOST}:{PORT}") as channel:
            message = self.handle_request(request)
            return message

    #Recibe
    def GetSendMessage(self, request, context):
        message = self.handle_request(request)
        result = messages_pb2.Result(result=message)
        return result

    @staticmethod
    def handle_request(request) -> Optional[Dict]:
        op = request.op.value
        if op == Ops.CREATE.value:
            queue_name = getattr(request, 'queue_name', None)
            create_queue(queue_name)
        elif op == Ops.POST.value:
            pass
        elif op == Ops.GET.value:
            pass
        else:
            pass
        return{}

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessagesServicer_to_server(MessagesServicer(), server)
    server.add_insecure_port(f"{HOST}:{PORT}")
    server.start()
    print(f'Servidor en ejecución en el puerto {PORT}...')
    server.wait_for_termination()


class Ops(Enum):
    CREATE = 'create'
    POST = 'post'
    GET = 'get'
