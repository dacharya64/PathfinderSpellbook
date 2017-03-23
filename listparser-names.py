# rewrites names of spells for the LIST_OF_SPELLS Alexa needs

import json

# file to which we will be writing spell names and descriptions
fWrite = open('spellnames.txt', 'w')

# opens the JSON file with the spell data and saves it to a JSON object
with open('spells.json') as data_file:
    data = json.load(data_file)

# runs through each spell in JSON object and extracts the data, writing it to file
# encodes characters and replaces apostrophes with escape character
for item in data:
    name = item["fields"]["name"].encode("utf-8").lower()
    # nameEscaped = name.replace("\'", "\\'")
    # desc = item["fields"]["short_description"].encode("utf-8")
    # descEscaped = desc.replace("\'", "\\'")
    fWrite.write(name + '\n')

fWrite.close()
