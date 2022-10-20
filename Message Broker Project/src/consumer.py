from amqpstorm import Connection, Message

class Consumer :
    def __init__(self, hostname, username, password) :
        self.connection = Connection(hostname, username, password) 
        
    
    def on_message(self, message):
        
        print('Consume Message Body ' + message.body)
        
        print(message.properties)
        
        print(message)
         
         
    def consume(self) :
        with self.connection.channel() as channel :
            
            channel.queue.declare('simple_queue') 
            
            channel.basic.qos(100)
                    
            channel.basic.consume(self.on_message, 'simple_queue', no_ack=False)
            
            try :
                channel.start_consuming() 
            except KeyboardInterrupt as e :
                print(e)
                channel.close()


if __name__ == '__main__' :
    consumer = Consumer('localhost', 'guest', 'guest')
    consumer.consume()
                
                