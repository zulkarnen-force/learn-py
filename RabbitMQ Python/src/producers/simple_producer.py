from wsgiref import headers
from amqpstorm import Connection, Message


class Producer :
    __conection = Connection('localhost', 'guest', 'guest');
    __channel = __conection.channel();
    __channel.queue.declare('surat') 
    __message = Message.create(__channel, body="simple email", properties={
        "content_type" : "none",
        "headers": {
            'filename':'example-filename'
        }
    })
    
    __message.publish('surat')
    
    
simple = Producer()
