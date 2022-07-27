
n, m = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if array[i] > m:
        continue
    elif array[i] == m:
        cnt+=1
        continue
    for j in range(i, n):
        if sum(array[i:j+1]) > m:
            break
        elif sum(array[i:j+1]) == m:
            cnt += 1
            break

print(cnt)
