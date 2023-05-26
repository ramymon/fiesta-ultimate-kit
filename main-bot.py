# Calling all needed pakages and functions (Regrouped in one file ) :
from dependencies import *




data_file = 'bot-memory-data.json'
print(data_file)
# Calling Data from json file :
#with io.open(data_file, "r", encoding="utf-8") as file:
with open(data_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print(data["base_yin_rel"])