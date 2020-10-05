import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_964769.html'
html = urllib1.request.urlopen(url).read()
# remember ! .read is a method seen in file handling , it means that all
# the result will be returned in one big string instead of reading line by line
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the li
tags = soup('span')
values = list()
for tag in tags:
    values.append(int(tag.text))
print(sum(values))