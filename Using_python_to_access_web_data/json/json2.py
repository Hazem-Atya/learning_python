import json

data='''{
  "name": "Hazem",
  "Age": 21,
  "phone": {
    "type": "intl",
    "number": ",+21625969655"
  },
  "email": {
    "hide": "yes"
  }
}'''
p = json.loads(data)
# p is a dictionary
print(p)
