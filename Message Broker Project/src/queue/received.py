from  amqpstorm import Connection

connection = Connection('localhost', 'guest', 'guest')

channel = connection.channel()

def cb(message):
    
    print(message.body)
    
    message.ack()

channel.basic.consume(cb, 'hello', no_ack=False)

channel.start_consuming()

