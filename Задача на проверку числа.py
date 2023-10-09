a = int(input())
b = 0

for с in range(1, a + 1):
    if (a % с == 0):
        b += 1
if (b == 2):
    print('Число простое')
else:
    print('Число не простое')