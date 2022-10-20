class One: pass




import abc

class Muka(abc.ABC):

    def kelas():
        pass
    
    @abc.abstractclassmethod
    def get(nama):
        pass

class Manusia(Muka):
    
    
    def get(self):
        return 'manusia'


manusia = Manusia()
