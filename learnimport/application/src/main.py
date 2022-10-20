from hashlib import new
from application.databases.sql.ConnectionSaja import ConnectionSaja
config = {"hostname": "localhost", "port": 5000, "bukan": "bukan port biasa"}

ConnectionSaja(**config)
