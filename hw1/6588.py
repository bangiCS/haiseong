#
# def is_sosu(n):
#     if n < 2:
#         return 0
#
#     i = 2
#     while i**2 <= n:
#         if n%i==0:
#             return 0
#         i+=1
#     return 1
#
#
# while True:
#     n = int(input())
#
#     if not 6 <= n <=1000000:
#         break
#
#     is_solved = 0
#     for a in range(2, n//2+1):
#         if is_sosu(a):
#             b = n-a
#             if is_sosu(b):
#                 print('%d = %d + %d'%(n, a, b))
#                 is_solved = 1
#                 break
#     if is_solved == 0:
#         print("Goldbach's conjecture is wrong.r")

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

while True:
    n = int(input())

    if not 6 <= n <=1000000:
        break

    is_solved = 0
    for a in primes:
        b = n-a
        if b in primes[::-1]:
            print("%d = %d + %d"%(n,a,b))
            is_solved = 1
            break

    if is_solved == 0:
        print("Goldbach's conjecture is wrong.r")
