from email import message
from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World'
)

connection.close()
