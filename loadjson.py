# Python program to read
# json file
import json
# Opening JSON file
f = open('cards.json')
# returns JSON object as 
# a dictionary
data = json.load(f)
# Iterating through the json
# list

print(data["Linux Modules"]["M1"])

for i in data["Linux Modules"]["M1"]:
    print(i)
 
# Closing file
f.close()
