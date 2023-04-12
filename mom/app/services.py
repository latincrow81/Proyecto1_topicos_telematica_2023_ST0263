import grpc
from concurrent import futures
from enum import Enum

from app.controllers import create_queue, push_message_to_queue, pop_message_from_queue
from dotenv import dotenv_values

from app.protos import mom_pb2_grpc, mom_pb2

config = dotenv_values(".env")

SERVER_ADDRESS = config.get('HOST_MOM')
GRPC_PORT = config.get('PORT_MOM')


class Handler(mom_pb2_grpc.MessageQueueServicer):
    def PushMessage(self, request, context):
        if request.op == Ops.CREATE.value:
            queue_name = request.queue_name
            response = create_queue(queue_name)
            return mom_pb2.QueueResponse(result=str(response))
        elif request.op == Ops.POST.value:
            queue_name = request.queue_name
            payload = request.payload
            response = push_message_to_queue(queue_name, payload)
            return mom_pb2.QueueResponse(result=str(response))
        else:
            pass

    def PullMessage(self, request, context):
        if request.op == Ops.GET.value:
            queue_name = request.queue_name
            response = pop_message_from_queue(queue_name)
            return mom_pb2.MessageResponse(payload=response)
        else:
            pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mom_pb2_grpc.add_MessageQueueServicer_to_server(Handler(), server)
    server.add_insecure_port('[::]:' + GRPC_PORT)
    server.start()
    print(f'Servidor en ejecución en el puerto {GRPC_PORT}...')
    server.wait_for_termination()


class Ops(Enum):
    CREATE = 'create'
    POST = 'post'
    GET = 'get'
