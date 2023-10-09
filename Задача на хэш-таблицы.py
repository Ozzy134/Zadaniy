a = input()

f = a.split()

b = {}
for c in f:
    if c in b.keys():
        b[c] += 1
    else:
        b[c] = 1
key = max(b, key = b.get)

print(key, b[key])