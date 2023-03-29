import os

import grpc

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

SERVER_ADDRESS = os.getenv("HOST_MOM")
SERVER_PORT = os.getenv("PORT_MOM")


def send_message(queue_name):
    with grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}") as channel:

        stub = files_pb2_grpc.MessagesStub(channel)
        response = stub.CreateQueue(files_pb2.QueueMessage(queue_name=queue_name))

    return response.message
