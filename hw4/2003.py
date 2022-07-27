
n, m = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
while end < n:
    temp = sum(array[start:end+1])
    if temp == m:
        cnt += 1
        start+=1
        end+=1
    elif temp<m:
        end+=1
    else:
        start+=1

print(cnt)
