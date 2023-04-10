import grpc
from dotenv import dotenv_values
from api_gateway.app.protos import messages_pb2_grpc, messages_pb2

config = dotenv_values("../.env")

HOST = config.get('HOST')
PORT = config.get('PORT')


def send_message(message: messages_pb2.Message) -> str:
    with grpc.insecure_channel(f"{HOST}:{PORT}") as channel:
        stub = messages_pb2_grpc.MessagesStub(channel)
        message_pb = messages_pb2.Message(queue_name=message.queue_name, op=message.op, payload=message.payload)
        response = stub.GetSendMessage(message_pb)
    return response.result