class DBConnect:
    
    def __init__(self, **config) -> None:
        print(config)
        self.host = config.get('host')
        self.port = config.get('port')
        self.username = config.get('username')
        return None
        
        
        
    def info(self):
        print(self)

    

