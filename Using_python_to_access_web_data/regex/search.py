import re

hand = open("mbox-short.txt")

for line in hand:
    if re.search('X-\S+:', line):
        print(line)
