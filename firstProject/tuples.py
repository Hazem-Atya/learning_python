x = ('Hazem', 'Atya', 21)
print(x)
for i in x:
    print(i)
# Unlike lists , we can't change tuples

(x, y) = ('Safa', 18)
print(x)

d = {'x': 10, 'b': 1, 'c': 22}
tri = sorted(d.items())
print(tri)

# ----------------sort a dictionary by value---------------
tmp = list()

for k, v in d.items():
    tmp.append((v, k))

print(tmp)
tmp = sorted(tmp)
print(tmp)
rev = sorted(tmp, reverse=True)
print(rev)

