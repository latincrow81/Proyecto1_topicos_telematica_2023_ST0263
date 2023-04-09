import os
import grpc
from concurrent import futures
from enum import Enum
from typing import Optional, Dict

from controllers import create_queue
from protos import messages_pb2_grpc

SERVER_ADDRESS = os.getenv("HOST_MOM")
GRPC_PORT = os.getenv("PORT_MOM")


class ListFilesServicer(messages_pb2_grpc.MessagesServicer):

    # Abre conexión
    def handle_grpc_request_from_gateway(self, request, context):

        with grpc.insecure_channel("localhost:50051") as channel:

            message = self.handle_request(request)
            return message

    @staticmethod
    def handle_request(request) -> Optional[Dict]:
        if request['op'] is Ops.CREATE:
            queue_name = request.get('queue_name')
            create_queue(queue_name)
        elif request['op'] is Ops.POST:
            pass
        elif request['op'] is Ops.GET:
            pass
        else:
            pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessagesServicer_to_server(messages_pb2_grpc.MessagesServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print(f'Servidor en ejecución en el puerto {GRPC_PORT}...')
    server.wait_for_termination()


class Ops(Enum):
    CREATE = 'create'
    POST = 'post'
    GET = 'get'
