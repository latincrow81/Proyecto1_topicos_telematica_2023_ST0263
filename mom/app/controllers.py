import os


host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue():
    return

def push_message_to_queue():
    return

def pop_message_from_queue():
    return