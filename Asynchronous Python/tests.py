class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
class Cat():

    def __init__(self, color: str) -> None:
        self._color = color
        
    @property 
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    
cat = Cat("brown")
print(getattr(cat, "None"))
print(cat.color)
cat.color = 'black'
print(cat.color)
