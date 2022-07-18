
from collections import deque
n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    temp = list(input())
    graph.append(list(map(int,temp)))

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
dd = [(1,0), (0,1) ,(-1,0), (0,-1)]

queue = deque([(0,0,0)])
visited[0][0][0] = 1
while queue:
    y,x,wall = queue.popleft()
    if y==n-1 and x==m-1:
        print(max(visited[y][x]))
        exit(0)
    for i in range(4):
        ny, nx = y + dd[i][0], x + dd[i][1]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 0 and visited[ny][nx][wall] == 0 :
                visited[ny][nx][wall] =  visited[y][x][wall] + 1
                queue.append((ny,nx,wall))
            elif graph[ny][nx] == 1 and wall < k :
                if visited[ny][nx][wall + 1] == 0:
                    visited[ny][nx][wall+1] = visited[y][x][wall] + 1
                    queue.append((ny,nx,wall+1))

print(-1)