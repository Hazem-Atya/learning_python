n = 10
while n > 0:
    print(n)
    n = n - 1
print("--------------------------------")

while True:
    msg = input(">")
    if msg == "done":
        break
# don't forget "continue"
print("--------------------------------")

for i in [0, 2, 4, 6, 8]:
    print(i)
print("--------------------------------")

for i in ["Hazem", "Safa", "Youssef"]:
    print(i)
print("--------------------------------")
langues=["Français", "Arabic", "English"]
for langue in langues:
    print(langue)