# WAP using function to find greatest of three numbers.

def greatest(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > a):
        return c

a = 10
b = 22
c = 3

print(greatest(a, b, c))