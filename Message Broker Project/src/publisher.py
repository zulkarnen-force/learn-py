from amqpstorm import Connection, Message
import json



with Connection('localhost', 'guest', 'guest') as connection :
    with connection.channel() as channel :

        channel.queue.declare('simple_queue')

        message = Message.create(channel, "filename", {'content_type': 'text/xls', 'headers': {'filename': 'data.json'} })
        
        # publish message ke queue 'files'
        message.publish('simple_queue')
        
        


# import logging

# from amqpstorm import Connection
# from amqpstorm import Message

# logging.basicConfig(level=logging.INFO)

# with Connection('localhost', 'guest', 'guest') as connection:
#     with connection.channel() as channel:
#         # Declare the Queue, 'simple_queue'.
#         channel.queue.declare('simple_queue')

#         # Message Properties.
#         properties = {
#             'content_type': 'text/plain',
#             'headers': {'key': 'value'}
#         }

#         # Create the message.
#         message = Message.create(channel, 'Hello Dunia!', properties)

#         # Publish the message to a queue called, 'simple_queue'.
#         message.publish('files')