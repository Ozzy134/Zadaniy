a = input()

b = a.split()

for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i] > b[j]:
           b[i], b[j] = b[j], b[i]

print(b)
