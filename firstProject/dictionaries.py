d = dict()
d['name'] = 'Hazem'
d['age'] = 21
print(d)
print(d['age'])

counts = dict()
names = ['Hazem', 'Safa', 'Hazem', 'Sihem', 'Safa', 'Hazem']

# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
#
# print(counts)

# Deuxième méthode
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # counts.get(name, 0) = counts[name] if it exists and 0 if not
print(counts)

# counts = dict()
# line = input('Enter a line of text :')
# words = line.split()
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print(counts)

for key in counts:
    print(counts[key])

keys = counts.keys()  # same as keys=list(counts)
print(keys)

values = counts.values()
print(values)

both = counts.items()  # a list of the tuples
print(both)
type(counts)
for a, b in both:
    print(a, ":", b)

