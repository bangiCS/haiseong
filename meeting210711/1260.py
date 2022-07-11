from collections import deque

n, m, v = map(int, input().split())

graph = dict()
for i in range(1,n+1):
    graph[i] = []
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for g in graph:
    graph[g].sort()

# dfs
visited = [False] * (n+1)
def dfs(x):
    visited[x] = True
    print(x, end = ' ')
    for y in graph[x]:
        if visited[y] == False:
            dfs(y)

dfs(v)
print()

# bfs
queue = deque([v])
visited = [False] * (n+1)
visited[v] = True
while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next in graph[now]:
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
print()