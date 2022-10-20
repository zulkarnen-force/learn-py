import amqpstorm

def on_message(message):
    print(message.body)

c = amqpstorm.Connection('localhost', 'guest', 'guest')
ch = c.channel()

ch.exchange.declare(exchange='logs', exchange_type='fanout')

result = ch.queue.declare(queue='', exclusive=True)

queue_name = result['queue']

ch.queue.bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(message):
    print(" [x] %r" % message.body)

ch.basic.consume(callback, queue_name, no_ack=False)

ch.start_consuming()