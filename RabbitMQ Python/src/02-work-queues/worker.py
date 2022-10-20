import queue
import time
from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body) :
    print(' [x] Received {}'.format(body.decode()))
    time.sleep(body.count(b'.') )
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
    
channel.basic_consume(
    queue='hello',
    on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()