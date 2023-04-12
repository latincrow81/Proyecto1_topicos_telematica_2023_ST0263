from flask import Response, request

from app.protos import mom_pb2
from .services import send_message, get_message


# Manda mensaje para que la cola se cree


def list_queues() -> Response:
    message = mom_pb2.QueueRequest(queue_name='', op='list', payload='')
    grpc_response = get_message(message)
    return Response(status=200, response=grpc_response)


def create_queue(queue_name: str) -> Response:
    message = mom_pb2.QueueRequest(queue_name=queue_name, op='create', payload='')
    grpc_response = send_message(message)
    return Response(status=200, response=f"Cola creada como {queue_name}, {grpc_response}")


# Manda un request de Grpc para meter un mensaje en la cola
def post_to_queue(queue_name: str) -> Response:
    request_data = request.json
    payload = request_data.get('data')
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='post', payload=payload)
    grpc_response = send_message(queue_message)

    return Response(status=200, response=f"Mensaje enviado a cola {queue_name}, {grpc_response}")


def delete_queue(queue_name: str) -> Response:
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='delete')
    grpc_response = send_message(queue_message)

    return Response(status=200, response=f"Cola {queue_name} eliminada correctamente, {grpc_response}")


# (POP) Lee el ultimo mensaje de la cola
def read_from_queue(queue_name: str) -> Response:
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='get')
    grpc_response = get_message(queue_message)

    return Response(status=200, response=f"{grpc_response}")

def list_topics() -> Response:
    message = mom_pb2.TopicRequest(topic_name='', op='list', payload='')
    grpc_response = get_topic(message)
    return Response(status=200, response=grpc_response)


def create_queue(queue_name: str) -> Response:
    message = mom_pb2.QueueRequest(queue_name=queue_name, op='create', payload='', type='Q')
    grpc_response = send_message(message)
    return Response(status=200, response=f"Cola creada como {queue_name}, {grpc_response}")


# Manda un request de Grpc para meter un mensaje en la cola
def post_to_queue(queue_name: str) -> Response:
    request_data = request.json
    payload = request_data.get('data')
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='post', payload=payload, type='Q')
    grpc_response = send_message(queue_message)

    return Response(status=200, response=f"Mensaje enviado a cola {queue_name}, {grpc_response}")


def delete_queue(queue_name: str) -> Response:
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='delete', type='Q')
    grpc_response = send_message(queue_message)

    return Response(status=200, response=f"Cola {queue_name} eliminada correctamente, {grpc_response}")


# (POP) Lee el ultimo mensaje de la cola
def read_from_queue(queue_name: str) -> Response:
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='get', type='Q')
    grpc_response = get_message(queue_message)

    return Response(status=200, response=f"{grpc_response}")
