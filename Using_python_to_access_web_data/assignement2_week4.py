import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# remember ! .read is a method seen in file handling , it means that all
# the result will be returned in one big string instead of reading line by line

# Retrieve all the li

i = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Ole.html'
while i < 7:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[17].get('href', None)
    i = i + 1
print(tags[17].text)
