import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True) # akan generate queue name random amq.gen-JzTY20BRgKO-HjmUJj0wLg

message = ' '.join(sys.argv[1:]) or 'Hello World'

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

channel.queue_bind(
    exchange='logs',
    queue=result.method.queue
)

print(f' [x] sent message with {message}')

connection.close(200, 'Sangat Normal Shutdown')
