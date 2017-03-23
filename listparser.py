# takes JSON list of spells and extracts name and short description,
# and writes these to file spellsparsed in a way that they can be
# used within recipes.js

import json

# file to which we will be writing spell names and descriptions
fWrite = open('spellsparsed.txt', 'w')

# opens the JSON file with the spell data and saves it to a JSON object
with open('spells.json') as data_file:
    data = json.load(data_file)

# runs through each spell in JSON object and extracts the data, writing it to file
# encodes characters and replaces apostrophes with escape character
for item in data:
    name = item["fields"]["name"].encode("utf-8")
    nameEscaped = name.replace("\'", "\\'")
    desc = item["fields"]["short_description"].encode("utf-8")
    descEscaped = desc.replace("\'", "\\'")
    fWrite.write("'" + nameEscaped + "': " + "'" + descEscaped + "',\n")

fWrite.close()
