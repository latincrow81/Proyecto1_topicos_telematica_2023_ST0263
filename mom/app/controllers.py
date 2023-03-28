import os

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue(queue_name):
    # todo: crear espacio en memoria comparida con queue_name
    return None

def push_message_to_queue(queue_name, payload):
    lista_queue_stack = list()
    lista_queue_stack.append(payload)
    # meter en memoria lista_queue_stack compartida
    # todo: push en stack payload en memoria compartida
    return

def pop_message_from_queue(queue_name):
    # todo: pop en stack de memoria compartida
    lista_queue_stack = list()
    response = lista_queue_stack.pop()

    return response