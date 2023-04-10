import json
import os
from multiprocessing.shared_memory import ShareableList

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


# Controllador para operaciones de cola, como mvp todas las colas son de profundidad 5 y ordenamiento FIFO

def create_queue(queue_name):     
    shared_memory_list = ShareableList([' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024], name=queue_name)
    return shared_memory_list


def push_message_to_queue(queue_name, payload):
    temp_list = ShareableList(name=queue_name)
    for j in range(5):
        if temp_list[j] == ' ' * 1024:
            temp_list[j] = json.dumps(payload)
            return temp_list
        else:
            continue
    return temp_list


def pop_message_from_queue(queue_name):
    temp_list = ShareableList(name=queue_name)
    for j in range(5):
        if temp_list[j] == ' ' * 1024:
            continue
        else:
            value = temp_list[j]
            temp_list[j] = ' ' * 1024
            return value
