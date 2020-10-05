t = [1, [2, 4], 3]
print(t)

names = ['Hazem', 'safa', 'youssef']
for name in names:
    print(name)

names[0] = "Sihem"  # We cannot do this with strings
i = 0
print(len(names))
while i < len(names):
    print(names[i])
    i = i + 1

x=list(range(5))
print(x)

for i in range(len(names)):
    print(i, names[i])

# concatenating strings
a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9, 10, 11]
c = a + b
print(c)

# slicing
t = b[2:6]
print(t)

stuff = list()  # equivalent : stuff=[]
stuff.append("Hazem")
stuff.append(21)
print(stuff)

if not 'Safa' in stuff:
    print("Safa is not  here")
names = ['safa', "zakarya", "ali", "hazem"]
names.sort()
print(names)

numbers = [11, 25, 111, 222, 30]
numbers.sort()
print(numbers)

print("Small number", min(numbers))
print("Biggest number", max(numbers))
print("Somme", sum(numbers))
print("Average", sum(numbers) / len(numbers))

ch = "One Two Three"
t = ch.split()
print(t)

ch = "One_Tw o_Three"
t = ch.split('_')
print(t)

ch = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
t = ch.split()
v = t[1].split('@')
w = v[1].split('.')
print(ch.split()[1].split('@')[1].split('.')) #equivalent à print(w)
