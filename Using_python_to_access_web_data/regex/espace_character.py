import re

ch = "Hey my pc costs 1000"
ch1 = "Hey my pc costs 1000$"
res = re.findall("[0-9]+$", ch)
print(res)

res1 = re.findall("[0-9]+\$", ch1)
print(res1)
