import json
import os

import grpc
from flask import Response

from api_gateway.protos.generated import files_pb2_grpc

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def get_file_list():
    with grpc.insecure_channel(f'{host_grpc}:{grpc_port}') as channel:
        # Cliente para el servicio de ListFiles
        list_files_client = files_pb2_grpc.MessagesStub(channel)

        # Se llama al servicio de ListFiles
        response = list_files_client.GetSendMessage(files_pb2.ListFilesRequest())

        # Se retorna la lista de archivos en formato JSON
    return Response(status=200, response=json.dumps({"files": [file.filename for file in response.files]}))


def find_file():
    return Response(status=404, response={"error": "Archivo no encontrado"})
