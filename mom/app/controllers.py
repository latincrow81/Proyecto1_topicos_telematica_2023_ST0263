import os
import multiprocessing

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue(queue_name):
    shm = multiprocessing.shared_memory.SharedMemory(create=True, size=2048) 
    lista_queue_stack = shm.buf
    lista_queue_stack[0] = 0 
    return shm.name

def push_message_to_queue(queue_name, payload):
    shm = multiprocessing.shared_memory.SharedMemory(name=queue_name)
    lista_queue_stack = shm.buf
    lista_queue_stack[lista_queue_stack[0] + 1] = payload
    lista_queue_stack[0] += 1
    shm.close()

def pop_message_from_queue(queue_name):
    shm = multiprocessing.shared_memory.SharedMemory(name=queue_name)
    lista_queue_stack = shm.buf
    response = lista_queue_stack[lista_queue_stack[0]]
    lista_queue_stack[0] -= 1
    shm.close()
    return response
