from flask import Response, request

from app.protos import mom_pb2
from .services import send_message, get_message, send_message_topic, get_message_topic


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


# (POP) Lee el último mensaje de la cola
def read_from_queue(queue_name: str) -> Response:
    queue_message = mom_pb2.QueueRequest(queue_name=queue_name, op='get')
    grpc_response = get_message(queue_message)

    return Response(status=200, response=f"{grpc_response}")


# lista los tópicos disponibles
def list_topics() -> Response:
    message = mom_pb2.TopicRequest(topic_name='', op='list', payload='')
    grpc_response = get_message_topic(message)
    return Response(status=200, response=grpc_response)


# crea un nuevo tópico en memoria y lo guarda en la lista de tópicos
def create_topic(topic_name: str) -> Response:
    message = mom_pb2.TopicRequest(topic_name=topic_name, op='create', payload='')
    grpc_response = send_message_topic(message)
    return Response(status=200, response=f"Topico creado como {topic_name}, {grpc_response}")


# envía mensaje a tópico
def post_to_topic(topic_name: str) -> Response:
    request_data = request.json
    payload = request_data.get('data')
    queue_message = mom_pb2.TopicRequest(topic_name=topic_name, op='post', payload=payload)
    grpc_response = send_message_topic(queue_message)

    return Response(status=200, response=f"Mensaje publicado en topico {topic_name}, {grpc_response}")


# elimina tópico de la lista y lo remueve de memoria
def delete_topic(topic_name: str) -> Response:
    queue_message = mom_pb2.TopicRequest(topic_name=topic_name, op='delete')
    grpc_response = send_message_topic(queue_message)

    return Response(status=200, response=f"Topico {topic_name} eliminado correctamente, {grpc_response}")


# lee el mensaje en el tópico
def read_from_topic(topic_name: str) -> Response:
    queue_message = mom_pb2.TopicRequest(topic_name=topic_name, op='get')
    grpc_response = get_message_topic(queue_message)

    return Response(status=200, response=f"{grpc_response}")
