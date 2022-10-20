import json
import re
import requests

def get(url: str):
    with requests.get(url) as req:
        print(list(req.raw))
        return req.json()  
    
response = get("http://api.open-notify.org/astros.json")

print(type(response))

# msg = response['message'] 
# people = response['people']
# print(people)

# def only(property: str, response: dict):
#     return response[property]
    
# print(requests.request.json())
# name = list(map(lambda name: name['name'], people))
# craft = list(map(lambda name: name['craft'], people))
# print(name, craft)

# print("\n")

# print(list(map(lambda name, craft: {'nama': name, 'craft': craft}, name, craft)) )


