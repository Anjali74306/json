# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
import json
x= {
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
sorted_json_data = json.dumps(x, sort_keys=True)
print(sorted_json_data)
# print(type(x))
# import json

# Array of JSON Objects
# products = [{"name": "HDD", "brand": "Samsung", "price": 100},
#             {"name": "Monitor", "brand": "Dell", "price": 120},
#             {"name": "Mouse", "brand": "Logitech", "price": 10}]

# # Read and print the original data
# print("The original data:\n{0}".format(products))
# # Convert into the JSON object after sorting
# sorted_json_data = json.dumps(products, sort_keys=True)
# # Print the sorted JSON data
# print("The sorted JSON data based on the keys:\n{0}".format(sorted_json_data))




