import os
from concurrent import futures

import grpc

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

SERVER_ADDRESS = os.getenv("HOST_MOM")
GRPC_PORT = os.getenv("PORT_MOM")


class ListFilesServicer(files_pb2_grpc.MessagesServicer):

    def handle_grpc_request_from_gateway(self, request, context):
        with grpc.insecure_channel(f'{SERVER_ADDRESS}:{GRPC_PORT}') as channel:
            # todo: crear cola en memoria
            return "cola creada en el servidor"


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    files_pb2_grpc.add_MessagesServicer_to_server(files_pb2_grpc.MessagesServicer(), server)
    server.add_insecure_port(f'[::]:{SERVER_ADDRESS}')
    server.start()
    print(f'Servidor en ejecución en el puerto {GRPC_PORT}...')
    server.wait_for_termination()

