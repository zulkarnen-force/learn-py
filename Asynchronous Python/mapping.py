# cells = []
# import re

# def delete_abjad(text: str):
#     pattern = "[A-Z]+"
#     rgx = re.match(pattern, text)
#     return rgx.pos


# print(delete_abjad(''))    
    
# for i in range(10):
#     cells.append(f'A,{i}')
# "".split()
# mapping = map(lambda row: f"D{row.split(',')[1]}", cells)

# print("Before", cells)
# print("After", list(mapping))

l = [0, 1]
m = map(str, l)
print(list(m))