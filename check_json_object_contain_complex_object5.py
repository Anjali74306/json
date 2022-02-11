# json string ko check karo ki bo complex object contain karti hai ya nahi?


import json
x='{"5+3j":"complex"}'
print(type(x))
y=json.loads(x)
print(x)
print(type(y))

# it gives us error 