from amqpstorm import Connection
def on_message(ch):
    print(ch.channel.queue)
    print(ch.body)
    print('Method => {}'.format(ch.method))
    print('Properties => {}'.format(ch.properties))
    


class Consumer :
    

    connection = Connection('localhost', 'guest', 'guest')
    ch = connection.channel()
    ch.queue.declare('surat')
    ch.basic.consume(on_message, 'surat', no_ack=False)
    ch.start_consuming()


c = Consumer()