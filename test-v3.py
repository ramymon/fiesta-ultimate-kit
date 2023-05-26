
import json

data_file = 'bot-memory-data.json'

# Calling Data from json file :

with open(data_file, "r") as file:
    data = json.load(file)



  

print(data)