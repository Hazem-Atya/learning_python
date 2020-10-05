ch = "Bonjour"
# --------------------------------------
n = len(ch)  # Length of ch
print(n)
for letter in ch:
    print(letter)

print('Done')

ch1 = ch[0: 4]  # Bonj
print(ch1)

ch1 = ch[: 4]  # Bonj
print(ch1)

ch1 = ch[1:]  # onjour
print(ch1)

ch1 = ch[:]  # Bonjour
print(ch1)

print('na' in 'banana')  # True
print('za' in 'banana')  # false

ch = "Bonjour"
CH = ch.upper()
print(CH)
print("HELLO".lower())

ch = "banana"
pos = ch.find("na")
print(pos)

ch = "Hello Hazem Hazem"
new_ch = ch.replace("Hazem", "Safa")
print(new_ch)