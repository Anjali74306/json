# Q.3 Python object ko json string mai convert karne ka program likho?
import json
x={"name":"anjli","course":"merraki","hardwork":"True"}
print(type(x))
y=json.dumps(x)
print(x)
print(type(y))

