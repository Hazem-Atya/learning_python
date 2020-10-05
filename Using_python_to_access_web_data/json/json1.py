import json

f = open("person.json")
p = json.loads(f.read())
# p is a dictionary
print(p)
