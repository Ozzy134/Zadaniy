n = int(input())

a = 1
b = 0
c = 1

while c < n:
    b, a = b + a, b
    c += 1

print(b)