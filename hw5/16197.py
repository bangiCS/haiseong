import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
y1, x1 = -1, -1
y2, x2 = -1, -1

graph = [[True]*m for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == '#':
            graph[i][j] = False
        elif line[j] == 'o':
            if y1 == -1:
                y1, x1 = i, j
            else:
                y2, x2 = i, j

def bfs(y1, x1, y2, x2):
    start = (y1, x1, y2, x2, 0)
    queue = deque([start])

    while queue:
        y1, x1, y2, x2, depth = queue.popleft()
        if depth >= 10:
            print(-1)
            exit(0)

        for dy, dx in [(-1,0),(0,-1),(1,0),(0,1)]:
            ny1 = y1 + dy
            nx1 = x1 + dx
            ny2 = y2 + dy
            nx2 = x2 + dx
            if 0<=ny1<n and 0<=nx1<m and 0<=ny2<n and 0<=nx2<m:
                if graph[ny1][nx1] == True and graph[ny2][nx2] == True:
                    queue.append((ny1, nx1, ny2, nx2, depth + 1))
                elif graph[ny1][nx1] == True:
                    queue.append((ny1, nx1, y2, x2, depth + 1))
                elif graph[ny2][nx2] == True:
                    queue.append((y1, x1, ny2, nx2, depth + 1))
            elif 0<=ny1<n and 0<=nx1<m:
                print(depth + 1)
                exit(0)
            elif 0<=ny2<n and 0<=nx2<m:
                print(depth + 1)
                exit(0)
            else:
                continue

    if 0 <= ny1 < n and 0 <= nx1 < m and 0 <= ny2 < n and 0 <= nx2 < m:
        print(-1)
        exit(0)

bfs(y1,x1,y2,x2)