
import sys
input = sys.stdin.readline

n = 1000000
is_prime = [True] * (n+1)

for i in range(2, n+1):
    if is_prime[i] == True:
        for j in range(i*2, n+1, i):
            if is_prime[j] == True:
                is_prime[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(2, n):
        if is_prime[i] == True and is_prime[n-i] == True:
            print("%d = %d + %d"%(n,i,n-i))
            is_solved = True
            break
    if is_solved:
        continue
    else:
        print("Goldbach's conjecture is wrong.")