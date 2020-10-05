import urllib.request, urllib.parse , urllib.error

fhand = urllib.request.urlopen(
    'https://www.geeksforgeeks.org')

# fhand is a file handle , this is like opening a file with open()
for line in fhand:
    print(line.decode().strip())
