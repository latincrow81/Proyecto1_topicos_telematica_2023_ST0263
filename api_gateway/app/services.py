import os

import grpc


from dotenv import load_dotenv

from app.protos import messages_pb2_grpc, messages_pb2

load_dotenv()

HOST_GRPC = os.getenv('HOST_GRPC')
PORT_GRPC = os.getenv('PORT_GRPC')


def send_message(message: messages_pb2.Message) -> str:
    with grpc.insecure_channel(f"{HOST_GRPC}:{PORT_GRPC}") as channel:
        stub = messages_pb2_grpc.MessagesStub(channel)
        response = stub.GetSendMessage(message)

    return response.result

