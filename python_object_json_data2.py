# Python object ko json data main convert karne ka program likho?


import json
x= {
    "name": "David", 
    "class": "I", 
    "age": 6
}
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))

