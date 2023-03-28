import json
import os
import grpc
import requests
from flask import Response
from api_gateway.app.services import send_message
from api_gateway.protos.generated import files_pb2_grpc, files_pb2

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')

#Manda mensaje para que la cola se crea
def create_queue(request):
    # TODO: abrir conexion grpc enviar mensaje que incluya nombre de cola la respuesta debe ser un mensaje "cola creada <nombre>"
    # todo: enviar un diccionario con "queue_name" y "op": "create"

    queue_name = request.get('queue_name')
    response_message = send_message(queue_name)
    response_data = {'queue_name':queue_name, 'op':'create'}

    return Response(status=200, response=f"Cola creada {response_message}", data=response_data)


#Manda un request de Grpc para meter un mesnaje en la cola
def post_to_queue():
    # TODO: enviar mensaje con grpc igual que create queue  - mensaje = {'op': 'create|post|get'}
    with grpc.insecure_channel(f'{host_grpc}:{grpc_port}') as channel:
        # Cliente para el servicio de Messages
        list_files_client = files_pb2_grpc.MessagesStub(channel)
        # Se llama al servicio de send message
        list_files_client.GetSendMessage(files_pb2.SendMessageRequest())
        # Se retorna el resultado de la creacion
    return Response(status=200, response={"exito": "Mensaje enviado a la cola"})

#(POP) Lee el ultimo mensaje de la cola 
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
