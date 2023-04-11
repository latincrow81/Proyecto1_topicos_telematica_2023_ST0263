import json
from multiprocessing import shared_memory
from multiprocessing.shared_memory import ShareableList

from flask import current_app

from .momdb import db
from .models import Queue, Topic


# Controlador para operaciones de cola y topico, como mvp todas las colas y topicos son de profundidad 5 y ordenamiento FIFO

def create_queue(queue_name):
    with current_app.app_context():
        shared_memory_list = shared_memory.SharedMemory(create=True, size=5 * 1024, name=queue_name)
        queue = Queue(name=queue_name)
        db.session.add(queue)
        db.session.commit()
    return shared_memory_list


def delete_queue(queue_name):
    try:
        shared_memory_list = shared_memory.SharedMemory(name=queue_name)
        shared_memory_list.unlink()
        with current_app.app_context():
            queue = Queue.query.filter_by(name=queue_name).first()
            db.session.delete(queue)
            db.session.commit()
        return True
    except FileNotFoundError:
        return False


def push_message_to_queue(queue_name, payload):
    with current_app.app_context():
        shared_memory_list = shared_memory.SharedMemory(name=queue_name)
        temp_list = [json.loads(shared_memory_list.buf[(1024 * i):(1024 * (i + 1))].decode()) for i in range(5)]
        for j in range(5):
            if temp_list[j] is None:
                shared_memory_list.buf[(1024 * j):(1024 * (j + 1))] = json.dumps(payload).encode()
                return shared_memory_list
            else:
                continue
        return shared_memory_list


def pop_message_from_queue(queue_name):
    with current_app.app_context():
        shared_memory_list = shared_memory.SharedMemory(name=queue_name)
        temp_list = [json.loads(shared_memory_list.buf[(1024 * i):(1024 * (i + 1))].decode()) for i in range(5)]
        for j in range(5):
            if temp_list[j] is None:
                continue
            else:
                value = temp_list[j]
                shared_memory_list.buf[(1024 * j):(1024 * (j + 1))] = ' ' * 1024
                return value


def create_topic(topic_name):
    with current_app.app_context():
        shared_memory_list = shared_memory.SharedMemory(create=True, size=5 * 1024, name=topic_name)
        topic = Queue(name=topic_name)
        db.session.add(topic)
        db.session.commit()
    return shared_memory_list


def delete_topic(topic_name):
    try:
        shared_memory_list = shared_memory.SharedMemory(name=topic_name)
        shared_memory_list.unlink()
        with current_app.app_context():
            topic = Queue.query.filter_by(name=topic_name).first()
            db.session.delete(topic)
            db.session.commit()
        return True
    except FileNotFoundError:
        return False


def push_message_to_topic(topic_name, payload):
    with current_app.app_context():
        shared_memory_list = shared_memory.SharedMemory(name=topic_name)
        temp_list = [json.loads(shared_memory_list.buf[(1024 * i):(1024 * (i + 1))].decode()) for i in range(5)]
        for j in range(5):
            if temp_list[j] is None:
                shared_memory_list.buf[(1024 * j):(1024 * (j + 1))] = json.dumps(payload).encode()
                return shared_memory_list
            else:
                continue
        return shared_memory_list

def pop_message_from_topic(topic_name):
    with current_app.app_context():
        temp_list = ShareableList(name=topic_name)
        for j in range(5):
            if temp_list[j] == ' ' * 1024:
                continue
            else:
                value = temp_list[j]
                return value


def list_queues():
    queues = Queue.query.all()
    return [queue.name for queue in queues]


def list_topics():
    topics = Topic.query.all()
    return [topic.name for topic in topics]
