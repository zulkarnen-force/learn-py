from sqlite3 import connect
import unittest
import redis
import json
import unittest
r = redis.Redis('localhost', 6379)
class TestRedis(unittest.TestCase):

    alamat = {
        "kabupaten": "Majalengka",
        "kecematan": "Sumberjaya"
    }
    
    
    
    # def test_add(self):
    #     self.assertIsInstance(r.rpush('list', "bos"), int)
    #     self.assertIsInstance(r.rpush('list', json.dumps(self.alamat)), int)
    #     self.assertIsInstance(r.rpush('list', "Pega"), int)
    #     self.assertIsInstance(r.rpush('list', "Zulkarnen"), int)
    #     self.assertIsInstance(r.rpush('list', "Yoza"), int)

    
    def test_get(self):
        print(r.lrange("list", 0, -1))
        
    # def test_delete(self):
    #     self.assertEqual(r.delete("list"), 1, "testing ketika dihapus")
        


if __name__ == '__main__' :
    unittest.main()