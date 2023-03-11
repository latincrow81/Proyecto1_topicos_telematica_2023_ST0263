import pika


class RmqSubscriberService:

    def __init__(self):
        self.config = {
            'host': 'localhost',
            'port': 5672,
            'exchange': 'gateway',
            'queueName': 'Response',
            'bindingKey': 'response'
        }

    def _create_connection(self):
        parameters = pika.ConnectionParameters(host=self.config['host'],
                                               port=self.config['port'])
        return pika.BlockingConnection(parameters)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print('received new message for -' + binding_key)

    def listen_for_rmq_response(self):
        connection = self._create_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic')

        channel.queue_declare(queue=self.config['queueName'])

        channel.queue_bind(queue=self.config['queueName'],
                           exchange=self.config['exchange'],
                           routing_key=self.config['bindingKey'])

        channel.basic_consume(queue=self.config['queueName'],
                              on_message_callback=self.on_message_callback, auto_ack=True)
        print('[*]  Waiting for data for ' + self.config['queueName'] + '.To exit press CTRL+C')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()