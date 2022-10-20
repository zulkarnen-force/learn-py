import redis
import json
import unittest
import redis

r = redis.Redis('localhost', port=6379, db=0)

r.set('foo', 'bar')

result = r.get('foo')
