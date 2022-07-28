a,b,c=input().split(' ')
a=int(a)
b=int(b)
c=int(c)
maxOdd=(a+b+c)/3

while maxOdd%2==0:
    maxOdd/=2
    print(maxOdd)
if a==b and b==c:
    print(1)
elif (a+b+c)%6>0:
    print(0)
elif a%maxOdd>0 or b%maxOdd>0:
    print(0)
elif (a/maxOdd)%3==0 and (b/maxOdd)%3==0:
    print(0)
else:
    print(1)