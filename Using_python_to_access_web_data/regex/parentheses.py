import re

stream = open('mbox-short.txt')

res = list()
for line in stream:
    res = res + re.findall('^From (\S+@\S+)', line)

print(res)
# The parentheses are not a part of the match , they just mean that we extract
# only what's in the parentheses
# in this example we find the every string that starts with from the a space,
# then one or more non blank characters then @ then one or more non blank
# characters but we only extract what's in the parentheses


