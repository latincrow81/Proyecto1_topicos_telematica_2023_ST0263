import json
from multiprocessing.shared_memory import ShareableList

from app.models import Queue
from app.utils import get_db_connection


# Controllador para operaciones de cola, como mvp todas las colas son de profundidad 5 y ordenamiento FIFO

def create_queue(queue_name):
    # guardando nombre de cola en lista
    db = get_db_connection()
    queue = Queue(name=queue_name)
    db.session.add(queue)
    db.session.commit()
    # creando cola en memoria
    shared_memory_list = ShareableList([' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024], name=queue_name)
    return shared_memory_list


def push_message_to_queue(queue_name, payload):
    try:
        temp_list = ShareableList(name=queue_name)
        for j in range(5):
            if temp_list[j] == ' ' * 1024:
                temp_list[j] = json.dumps(payload)
                return temp_list
            else:
                continue
        return temp_list
    except FileNotFoundError:
        return f"Queue no encontrada: {queue_name}"


def pop_message_from_queue(queue_name):
    temp_list = ShareableList(name=queue_name)
    for j in range(5):
        if temp_list[j] == ' ' * 1024:
            continue
        else:
            value = temp_list[j]
            temp_list[j] = ' ' * 1024
            return value
