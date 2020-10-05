import re

stream = open('mbox-short.txt')

emails = list()
for line in stream:
    t = re.findall('[a-z,A-Z,.,-,_]+@[a-z,A-Z,.,-,_]+', line)
    if t:
        emails = emails + t
i = 0
for email in emails:
    print(email)
