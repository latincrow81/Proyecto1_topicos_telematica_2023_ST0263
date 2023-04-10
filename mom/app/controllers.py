import json
from multiprocessing.shared_memory import ShareableList
from momdb import db
from models import Queue, Topic


# Controllador para operaciones de cola y topico, como mvp todas las colas y topicos son de profundidad 5 y ordenamiento FIFO

def create_queue(queue_name):
    shared_memory_list = ShareableList([' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024], name=queue_name)
    return shared_memory_list


def delete_queue(queue_name):
    try:
        shared_memory_list = ShareableList(name=queue_name)
        shared_memory_list.unlink()
        queue = Queue.query.filter_by(name=queue_name).first()
        db.session.delete(queue)
        db.session.commit()
        return True
    except FileNotFoundError:
        return False


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


def create_topic(topic_name):
    shared_memory_list = ShareableList([' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024, ' ' * 1024], name=topic_name)
    return shared_memory_list


def delete_topic(topic_name):
    try:
        shared_memory_list = ShareableList(name=topic_name)
        shared_memory_list.unlink()
        topic = Topic.query.filter_by(name=topic_name).first()
        db.session.delete(topic)
        db.session.commit()
        return True
    except FileNotFoundError:
        return False


def push_message_to_topic(topic_name, payload):
    temp_list = ShareableList(name=topic_name)
    for j in range(5):
        if temp_list[j] == ' ' * 1024:
            temp_list[j] = json.dumps(payload)
            return temp_list
        else:
            continue
    return temp_list


def pop_message_from_topic(topic_name):
    temp_list = ShareableList(name=topic_name)
    for j in range(5):
        if temp_list[j] == ' ' * 1024:
            continue
        else:
            value = temp_list[j]
            temp_list[j] = ' ' * 1024
            return value


def list_queues():
    queues = Queue.query.all()
    return [queue.name for queue in queues]


def list_topics():
    topics = Topic.query.all()
    return [topic.name for topic in topics]
