import re

ch = "My 2 favourite numbers are 18 et 20"
t = re.findall("[0-9]+", ch)
print(t)

str = 'From: Hazem Atya to his sister : Safa Atya'

# Greedy matching (finds the largest strings that
res = re.findall('^F.+:', str)
print(res)
# res=From: Hazem Atya to his sister :

res = re.findall('^F.+?:', str)
print(res)


