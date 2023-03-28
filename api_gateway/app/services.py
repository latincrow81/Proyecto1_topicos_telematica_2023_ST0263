import os
from concurrent import futures

import grpc

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

SERVER_ADDRESS = os.getenv("HOST_MOM")
SERVER_PORT = os.getenv("PORT_MOM")


def send_message(queue_name):
    with grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}") as channel:

        stub = files_pb2_grpc.MessagesStub(channel)
        response = stub.CreateQueue(files_pb2.QueueMessage(queue_name=queue_name))

    return response.message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    files_pb2_grpc.add_MessagesServicer_to_server(files_pb2_grpc.MessagesServicer(), server)
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    print(f'Servidor en ejecución en el puerto {SERVER_PORT}...')
    server.wait_for_termination()
