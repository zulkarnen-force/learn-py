with open('test.json', 'w') as opened_file :
    opened_file.write("""        [
            {
                "data" :
                    {
                        "nama": "zulkarnen"
                    }
            }
        ]"""
    )
    

# file = open('some_file', 'w')
# try:
#     file.write('Hola!')
# finally:
#     file.close()

class File(object):
    def __init__(self, filename: str, mode: str):
        self.file = open(filename, mode)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, type, value, traceback):
        self.file.close()


with File('test.json', 'r') as file:
    print(file)
    
    