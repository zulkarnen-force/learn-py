from lib2to3.pgen2.tokenize import untokenize
from logging import exception
import queue
import unittest
import amqpstorm
import sys

connection = amqpstorm.Connection('localhost', 'guest', 'guest')
channel = connection.channel()
channel.exchange.declare("favorite_taxi", "direct")



class TestExchange(unittest.TestCase) :
    
    def test_connection(self):
    
        connection = amqpstorm.Connection('localhost', 'guest', 'guest')
        
        channel = connection.channel()
        
        channel.exchange.declare(exchange='logs', exchange_type='fanout')
        
        channel.basic.publish(exchange='logs', routing_key='routing_key_logs', body="message")
        
        result = channel.queue.declare(queue="")
        
        print(result)
        
        channel.queue.bind(exchange='logs', queue=result['queue'])
        
        message = "info: Hello World!"
        
        channel.basic.publish(exchange='logs', routing_key='', body=message)
        
        
if __name__ == '__main__' :
    unittest.main()