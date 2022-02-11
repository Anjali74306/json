# Q.1 Json data ko python object main convert karne ka program likho?.
import json
x='{"name":"anjali","class":"12","rollno":"12"}'
y=json.loads(x)
print(type(y))
print(x)

