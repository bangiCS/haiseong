from collections import deque

graph = dict()

n, m, v = map(int, input().split())

for i in range(1,n+1):
    graph[i] = []
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    graph[g].sort()

# print(graph)

# dfs
stack = deque([v])
visited = [False] * (n+1)
# visited[v] = True
answer = ''

while stack:
    now = stack.pop()
    if visited[now] == False:
        visited[now] = True
        print(now, end=' ')
        answer += str(now) + ' '
        for next in graph[now][::-1]:
            # print(next)
            # print(stack)
            stack.append(next)

print()
# bfs
queue = deque([v])
visited = [False] * (n+1)
visited[v] = True

while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next in graph[now]:
        # print(next)
        # print(queue)
        if visited[next] == False:
            queue.append(next)
            visited[next] = True