import urllib.request, urllib.parse, urllib.error
import json

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_964772.json")
data = fhand.read()

d = json.loads(data)
print(type(d['comments']))
s=0
for item in d['comments']:
   s=s+int(item["count"])
print(s)