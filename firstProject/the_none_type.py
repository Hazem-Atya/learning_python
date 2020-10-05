# finding the smallest number
smallest = None
for i in [5, 7, 9, 4, 2, 15, 17]:
    if smallest is None:
        smallest = i
    elif smallest > i:
        smallest = i

print(smallest)

# is and is not are logical operators
