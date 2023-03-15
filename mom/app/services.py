import os

import grpc

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

SERVER_ADDRESS = os.getenv("HOST_MOM")
SERVER_PORT = os.getenv("PORT_MOM")


def send_grpc_request():
    with grpc.insecure_channel(f'{SERVER_ADDRESS}:{SERVER_PORT}') as channel:
        for file in files_pb2_grpc.MessagesStub(channel).GetSendMessage(files_pb2.SendMessageRequest()).files:
            print(file.filename)


def get_file_list_grpc():
    pass

