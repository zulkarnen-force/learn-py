import unittest
import redis
import json
import pandas as pd

connection = redis.Redis('localhost', 6379)

class UnitTest(unittest.TestCase) :
    
    # def test_rpush(self):
    #     self.assertIsInstance(connection.rpush(1290, json.dumps({"jsonData":"data data"})), int)
        
    def test_set_redis(self):
        self.assertEqual((connection.set('nama', 'zulkarnen')), True)
        
        
    def test_get_data(self):
        self.assertEqual(connection.get('nama'), bytes('zulkarnen', 'utf-8'))
        self.assertIsInstance(connection.get('nama'), bytes)
        
    def test_convert_bytes_to_str(self):
        bytes_nama = connection.get('nama')
        self.assertIsInstance(bytes_nama.decode('utf-8'), str)



    def test_split(self):
        data = "aku ; adalah ; kamu yang ; tertinggal".split(' ; ')
        print(data)
        print(pd.array(data))
        
if __name__ == '__main__' :
    # u = UnitTest()
    # u.test_case();
    # u.test_test()
    unittest.main()
    