
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array.pop()
second = array.pop()

cnt = 0
answer = 0
for i in range(m):
    if cnt >= k:
        answer += second
        cnt = 0
    else:
        answer += first
        cnt += 1

print(answer)