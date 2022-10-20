from lib2to3.pgen2.tokenize import untokenize
from logging import exception
import queue
import unittest
import amqpstorm
import sys

connection = amqpstorm.Connection('localhost', 'guest', 'guest')

channel = connection.channel()

channel.queue.declare('hello')
# channel.queue.declare('hello')

# message = ' '.join(sys.argv[1:]) or 'hello word'

# MessageResponse = amqpstorm.Message.create(channel, message, properties={"content_type":"contoh content"})

channel.basic.publish(routing_key='', body="just message")