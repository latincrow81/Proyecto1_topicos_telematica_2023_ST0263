import os
import grpc
from flask import Response, request
from api_gateway.app.services import send_message
from api_gateway.protos.generated import files_pb2_grpc, files_pb2

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')

#Manda mensaje para que la cola se cree

def create_queue():
    request_data = request.json
    queue_name = request_data.get('queue_name')
    queue_message = {'queue_name': queue_name, 'op':'create'}
    response_message = send_message(queue_message)

    return Response(status=200, response=f"Cola creada {response_message}")


#Manda un request de Grpc para meter un mesnaje en la cola
def post_to_queue():
    request_data = request.json
    queue_name = request_data.get('queue_name')
    payload = request_data.get('payload')
    queue_message = {'queue_name': queue_name, 'op': 'post', 'payload': payload}
    send_message(queue_message)

    return Response(status=200, response=f"Mensaje enviado a cola {queue_name}")


#(POP) Lee el ultimo mensaje de la cola 
def read_from_queue():
    request_data = request.json
    queue_name = request_data.get('queue_name')
    queue_message = {'queue_name': queue_name, 'op': 'get'}
    response_message = send_message(queue_message)

    return Response(status=200, response=response_message)
