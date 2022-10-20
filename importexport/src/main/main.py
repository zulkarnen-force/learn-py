from src.databases.DBConnect import DBConnect
config = {"localhost": "localhost"}

poll = DBConnect(host="hostname")

poll.info()

