from asyncio import constants
from platform import architecture
import sys
from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'Hello World'

channel.basic_publish(
    exchange='direct_logs',
    body=message,
    routing_key=severity
)

print(" [x] Sent {}:{}".format(severity, message))

connection.close()