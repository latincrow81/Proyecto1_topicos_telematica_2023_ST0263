import json
import os

import grpc
from flask import Response

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue():
    # TODO: abrir conexion grpc enviar mensaje que incluya nombre de cola la respuesta debe ser un mensaje "cola creada <nombre>"
    with grpc.insecure_channel(f'{host_grpc}:{grpc_port}') as channel:
        # Cliente para el servicio de Messages
        list_files_client = files_pb2_grpc.MessagesStub(channel)
        # Se llama al servicio de send message
        response = list_files_client.GetSendMessage(files_pb2.SendMessageRequest())
        # Se retorna el resultado de la creacion
    return Response(status=200, response=json.dumps({"files": [file.filename for file in response.files]}))

def post_to_queue():
    # TODO: enviar mensaje con grpc igual que create queue
    return Response(status=200, response={"exito": "Mensaje enviado a la cola"})

def read_from_queue():
    # TODO: leer mensaje de cola con grpc
    # TODO: response es el mensaje que retorne la cola
    return Response(status=200, response={})
