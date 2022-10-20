from code import interact
from dataclasses import field
from re import I


def inc():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
        
a = inc()

for i in a:
    print(i)
    
    
def gen():
    for i in range(1, 10):
        yield i*10
        
print(next(gen()))


print(type(list(range(10))))

generator = (i for i in range(10))

print(type(generator)) # <class 'generator'>


string = "stringvalues"

iterator = iter(string) 


print(type(iterator)) # <class 'str_iterator'>

print('\n', next(iterator), '\n')

for i in range(4):
    print(next(iterator))
    
    
for i in range(2):
    print(next(iterator))