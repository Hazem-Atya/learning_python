import re

stream = open('mbox-short.txt')

numList = list()
for line in stream:
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numList.append(num)
print("Max :", max(numList))

