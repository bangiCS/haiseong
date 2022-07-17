from collections import deque
n, k = map(int,input().split())

queue = deque([n])
visited = {n:0}

while queue:
    if k in visited:
        # print(visited)
        print(visited[k])
        break
    now = queue.popleft()
    if now == k:
        print(visited[now])
        break

    for next in (now*2, now-1, now+1):
        if 0<=next<=100000 and next not in visited:
            queue.append(next)
            visited[next] = visited[now] + 1
