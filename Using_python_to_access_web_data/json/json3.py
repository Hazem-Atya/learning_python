import json

input = ''' [
    {
       "id":"001",
        "x":"2",
        "name":"Hazem"  
    },
    {
        "id":"002",
        "x":"4",
        "name":"Safa"  
    }
]'''
info = json.loads(input)
print("this json is a",type(info))
print('User count', len(info))
for item in info:
    print("Name", item['name'])
    print("ID", item["id"])
    print("X", item["x"])

