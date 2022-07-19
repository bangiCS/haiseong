
n = int(input())

cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if h == 3:
                cnt+=1
                continue
            elif m // 10 == 3 or m % 10 == 3:
                cnt+=1
                continue
            elif s // 10 == 3 or s % 10 == 3:
                cnt+=1
                continue

print(cnt)