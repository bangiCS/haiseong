from collections import deque

n,m = map(int, input().split())
visited = [0] * (n+1)

graph = dict()
for i in range(1,n+1):
    graph[i] = list()

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for start in range(1, n+1):
    if visited[start] == 0:
        queue = deque([start])
        visited[start] = start
        while queue:
            now = queue.popleft()
            for next in graph[now]:
                if visited[next] == 0:
                    visited[next] = start
                    queue.append(next)

print(len(set(visited[1:])))