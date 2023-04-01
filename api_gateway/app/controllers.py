import json
from flask import Response, request

from .protos import messages_pb2
from .services import send_message

#Manda mensaje para que la cola se cree


def create_queue(queue_name: str) -> Response:
    message = messages_pb2.Message(queue_name=queue_name, op='create', payload='')
    grpc_response = send_message(message)
    return Response(status=200, response=f"Cola creada {grpc_response}")


#Manda un request de Grpc para meter un mesnaje en la cola
def post_to_queue(queue_name: str) -> Response:
    request_data = request.json
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
