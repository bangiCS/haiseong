from collections import deque

n, m = map(int ,input().split())
dd = [(-1,0),(0,1),(1,0),(0,-1)]
graph = []
for _ in range(n):
    graph.append(list(map(int,list(input()))))

def bfs(graph, start):
    y, x = start
    queue = deque([start])
    graph[y][x] = 1
    while queue:
        now = queue.popleft()
        y,x = now
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 0:
                    queue.append((ny,nx))
                    graph[ny][nx] = 1


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
            bfs(graph, (i,j))

print(cnt)