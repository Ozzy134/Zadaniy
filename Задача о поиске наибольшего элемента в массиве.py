a = input()

def myMax(a):
    max = a[0]
    for x in a:
        if x > max:
            max = x
    return max

print(myMax(a))




