import grpc

from dotenv import dotenv_values

from api_gateway.app.protos import messages_pb2_grpc, messages_pb2

config = dotenv_values("../.env")

HOST_GRPC = config.get('HOST_GRPC')
PORT_GRPC = config.get('PORT_GRPC')


def send_message(message: messages_pb2.Message) -> str:
    with grpc.insecure_channel(f"{HOST_GRPC}:{PORT_GRPC}") as channel:
        stub = messages_pb2_grpc.MessagesStub(channel)
        response = stub.GetSendMessage(message)
    return response.result


