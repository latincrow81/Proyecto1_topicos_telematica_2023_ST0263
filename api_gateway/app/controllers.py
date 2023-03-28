import json
import os

import grpc
import requests
from flask import Response

from api_gateway.protos.generated import files_pb2_grpc, files_pb2

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue(request: requests):
    # TODO: abrir conexion grpc enviar mensaje que incluya nombre de cola la respuesta debe ser un mensaje "cola creada <nombre>"
    # todo: enviar un diccionario con "queue_name" y "op": "create"
    with grpc.insecure_channel(f"{host_grpc}:{grpc_port}") as channel:
        stub = my_proto_pb2_grpc.QueueServiceStub(channel)
        response = stub.CreateQueue(my_proto_pb2.QueueRequest(queue_name=queue_name))
    return f"cola creada {queue_name}"

def post_to_queue():
    # TODO: enviar mensaje con grpc igual que create queue  - mensaje = {'op': 'create|post|get'}
    with grpc.insecure_channel(f'{host_grpc}:{grpc_port}') as channel:
        # Cliente para el servicio de Messages
        list_files_client = files_pb2_grpc.MessagesStub(channel)
        # Se llama al servicio de send message
        list_files_client.GetSendMessage(files_pb2.SendMessageRequest())
        # Se retorna el resultado de la creacion
    return Response(status=200, response={"exito": "Mensaje enviado a la cola"})

def read_from_queue():
    # TODO: leer mensaje de cola con grpc
    # TODO: response es el mensaje que retorne la cola
    with grpc.insecure_channel(f'{host_grpc}:{grpc_port}') as channel:
        # Cliente para el servicio de Messages
        list_files_client = files_pb2_grpc.MessagesStub(channel)
        # Se llama al servicio de send message
        message = list_files_client.GetSendMessage(files_pb2.SendMessageRequest())
        # Se retorna el resultado de la creacion
    return Response(status=200, response=message)
