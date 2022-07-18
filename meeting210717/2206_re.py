
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dd = [(-1,0),(0,-1),(1,0),(0,1)]

queue = deque([(0,0,0)])
visited[0][0][0] = 1
while queue:
    y,x,wall = queue.popleft()
    for i in range(4):
        dy = y + dd[i][0]
        dx = x + dd[i][1]
        if 0<=dy<n and 0<=dx<m:
            if graph[dy][dx] == 0 and not visited[dy][dx][wall]:
                visited[dy][dx][wall] = visited[y][x][wall] + 1
                queue.append((dy,dx,wall))
            elif graph[dy][dx] == 1 and wall  == 0 and not visited[dy][dx][wall + 1]:
                visited[dy][dx][wall+1] = visited[y][x][wall] + 1
                queue.append((dy,dx,wall+1))


if visited[-1][-1][0] == 0 and visited[-1][-1][1] == 0:
    print(-1)
elif visited[-1][-1][0] == 0 or visited[-1][-1][1] == 0:
    print(max(visited[-1][-1]))
else:
    print(min(visited[-1][-1]))
