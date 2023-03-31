import grpc

from app.protos import messages_pb2_grpc, messages_pb2
from dotenv import dotenv_values

config = dotenv_values("../.env")

HOST_GRPC = config.get('HOST_GRPC')
PORT_GRPC = config.get('PORT_GRPC')


def send_message(message):
    with grpc.insecure_channel(f"{HOST_GRPC}:{PORT_GRPC}") as channel:

        stub = messages_pb2_grpc.MessagesStub(channel)
        response = stub.GetSendMessage(messages_pb2.Message(message))

    return response.message
