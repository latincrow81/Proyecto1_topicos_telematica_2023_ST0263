import os
from multiprocessing.shared_memory import SharedMemory, ShareableList

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue(queue_name):     
    shared_memory_list = ShareableList(name=queue_name)
    return shared_memory_list

def push_message_to_queue(queue_name, payload):
    temp_list = ShareableList(name=queue_name)
    temp_list.append(payload)    
    shared_memory_list = ShareableList(sequence=temp_list, name=queue_name)
    return shared_memory_list

def pop_message_from_queue(queue_name):
    temp_list = ShareableList(name=queue_name)
    response = temp_list.pop()    
    shared_memory_list = ShareableList(sequence=temp_list, name=queue_name)
    return response, shared_memory_list
