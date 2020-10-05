try:
    fich = open('mbox-short.txt', 'r')
except:
    print("File cannot be opened ")
    quit()

count = 0
# for line in fich:
#     line=line.rstrip()  # delete white spaces in the right because print adds a newline
#     if line.startswith('From'):
#         print(line)
#     count = count + 1
print("The file contains", count, "Lines")

# print(fich.read()) # print the whole file
for line in fich:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)
