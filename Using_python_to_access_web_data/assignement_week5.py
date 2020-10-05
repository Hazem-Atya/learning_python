import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen(
    'http://py4e-data.dr-chuck.net/comments_964771.xml')
data = fhand.read()
stuff = ET.fromstring(data)
lst = stuff.findall("comments/comment/count")
lst = [int(item.text) for item in lst]
print(sum(lst))
