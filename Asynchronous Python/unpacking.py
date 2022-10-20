data = {
    "data": "data",
    "status": True
    }

def connect(**config):
    print(config)


def connect_1(*test):
    print(test)
    
connect_1('sat', 'dua')

# connect(**data)
# connect('data')
connect(host="localhost")

def connection(hostname: str, username: str):
    print(hostname, username)
    

config_connection = {'hostname': '127.0.0.1', 'username': 'root'}

connection(**config_connection)

def connection(**config):
    print(config["hostname"], config["username"])
    
connection(**config_connection)


# print(config_connection)
# a, b = {**config_connection}
# print(f'this a {a}')


# two dictionay
one = {'status': True, 'message': 'this example data with status code'}
two = {'data': [1, 2, 3]}

# merge dictionary
merge_onetwo = {**one, **two}

print(merge_onetwo)

# unpacking
satu = {**one}

# aliases
uno = one

# check identity
print(one is satu) 

print(one is uno)

