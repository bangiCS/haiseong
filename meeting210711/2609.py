
a, b = map(int, input().split())

def gcd(a, b):
    if a < b:
        a,b = b,a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

gcd_ = gcd(a, b)
print("%d"%gcd_)
print("%d"%(a*b//gcd_))