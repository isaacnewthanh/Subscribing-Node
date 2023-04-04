import json

dictionary = data

json_object = json.dumps(dictionary, indent = 4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)