import json
import os

import grpc
from flask import Response

from api_gateway.protos.generated import files_pb2_grpc

host_grpc = os.getenv("HOST_GRPC")
grpc_port = os.getenv("PORT_GRPC")
rmq_user = os.getenv('USER')
rmq_password = os.getenv('PASSWORD')


def create_queue():
    pass
