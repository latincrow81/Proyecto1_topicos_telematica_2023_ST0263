import os
from concurrent import futures

from enum import Enum
from typing import Optional, Dict


import grpc
from api_gateway.protos.generated import files_pb2_grpc, files_pb2
from mom.app.controllers import create_queue

SERVER_ADDRESS = os.getenv("HOST_MOM")
GRPC_PORT = os.getenv("PORT_MOM")


class ListFilesServicer(files_pb2_grpc.MessagesServicer):

# Abre conexión
    def handle_grpc_request_from_gateway(self, request, context):

        with grpc.insecure_channel(f'{SERVER_ADDRESS}:{GRPC_PORT}') as channel: 

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
    files_pb2_grpc.add_MessagesServicer_to_server(files_pb2_grpc.MessagesServicer(), server)
    server.add_insecure_port(f'[::]:{SERVER_ADDRESS}')
    server.start()
    print(f'Servidor en ejecución en el puerto {GRPC_PORT}...')
    server.wait_for_termination()



class Ops(Enum):
    CREATE = 'create'
    POST = 'post'
    GET = 'get'