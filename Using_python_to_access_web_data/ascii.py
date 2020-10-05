print(ord('A'))
print(ord('\t'))

str = "حازم عطية"
# data = str.encode(encoding="UTF-8", errors="strict")
data = str.encode()
print(data)

test = b'\xd8\xad\xd8\xa7\xd8\xb2\xd9\x85 \xd8\xb9\xd8\xb7\xd9\x8a\xd8\xa9'
print(test.decode())

test2 = b'\x48\x61\x7a\x65\x6d'
print(test2.decode())