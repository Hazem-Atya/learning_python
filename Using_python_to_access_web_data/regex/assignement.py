import re

stream = open("regex_sum_964767.txt")
numbers = list()
for line in stream:
    t = re.findall('[0-9]+', line)
    t = [int(n) for n in t]
    numbers = numbers + t

print(sum(numbers))
