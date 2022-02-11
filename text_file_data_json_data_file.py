# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29


import json  
dict1={"Name": "Abhishek","Designation" :"CEO of navgurukul","Gender": "male","Age": "29"}
out_file = open("myfile.json", "w")
json.dump(dict1, out_file, indent = 6)
out_file.close()