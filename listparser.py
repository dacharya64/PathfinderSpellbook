# takes JSON list of spells and extracts name and short description,
# and writes these to file spellsparsed in a way that they can be
# used within recipes.js

import json
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


# file to which we will be writing spell names and descriptions
fWrite = open('spellsparsed.txt', 'w')

# opens the JSON file with the spell data and saves it to a JSON object
with open('spells.json') as data_file:
    data = json.load(data_file)
    # dataClean = cleanhtml(data)

# runs through each spell in JSON object and extracts the data, writing it to file
# encodes characters and replaces apostrophes with escape character
for item in data:
    name = item["fields"]["name"].encode("utf-8").lower()
    # nameEscaped = name.replace("\'", "\\'")
    desc = item["fields"]["short_description"].encode("utf-8")
    descClean = cleanhtml(desc)
    # descEscaped = desc.replace('\"', '\\"')
    fWrite.write("\"" + name + "\": " + "\"" + descClean + "\",\n")

fWrite.close()
