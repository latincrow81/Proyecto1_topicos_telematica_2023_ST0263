import os
from concurrent import futures
import grpc

from dotenv import load_dotenv

from protos import messages_pb2_grpc, messages_pb2
from .services import ListFilesServicer

load_dotenv()

ROOT_PATH = os.getenv("ROOT_PATH")
PORT = os.getenv("PORT")

#Recibe el mensaje
class MessageService(messages_pb2_grpc.MessagesServicer):

    def GetFilesList(self, request, context):
        print(f"Request: {request}")
        files = []
        for item in os.listdir(ROOT_PATH):
            item_path = os.path.join(ROOT_PATH, item)
            if os.path.isfile(item_path):
                files.append(messages_pb2.File(filename=item, file=bytes(item, encoding="utf-8")))
        response = messages_pb2.ListFilesResponse(files=files)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessagesServicer_to_server(ListFilesServicer(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    print(f'Servidor en ejecución en el puerto {PORT}...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
