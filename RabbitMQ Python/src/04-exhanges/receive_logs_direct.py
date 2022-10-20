import queue
from subprocess import call
import sys
from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)

result = channel.queue_declare(queue='',
                               exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]

if not severities :
    sys.stderr.write("Usage: {} [info] [warning] [error]\n".format(sys.argv[0]))
    sys.exit(1)

for severity in severities :
    channel.queue_bind(
        queue=queue_name,
        exchange='direct_logs',
        routing_key=severity
    )


print(f' [*] Waiting for log: {severity}. To exit press CTRL+C')


def callback(channel, method, properties, body):
    print(' [x] {}:{}'.format(method.routing_key, body))
    


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)


channel.start_consuming()