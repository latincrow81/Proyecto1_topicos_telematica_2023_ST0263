import pika


class RmqPublisherService:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'port': 5672,
            'exchange': 'topic'
        }

    def create_connection(self):
        param = pika.ConnectionParameters(host=self.config['host'],
                                          port=self.config['port'])
        return pika.BlockingConnection(param)

    def send_rmq_request(self):
        connection = self.create_connection()
        connection.channel()

