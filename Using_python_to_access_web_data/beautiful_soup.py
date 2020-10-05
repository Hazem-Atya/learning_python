import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter a url:")
html = urllib.request.urlopen(url).read()
# remember ! .read is a method seen in file handling , it means that all
# the result will be returned in one big string instead of reading line by line

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
