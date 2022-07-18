
n, k = map(int, input().split())

cnt = 0

while n>=k:
    if n % k ==0:
        n //= k
        cnt += 1
    else:
        cnt += n % k
        n -= n % k

cnt += n-1
print(cnt)