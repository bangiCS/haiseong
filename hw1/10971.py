import sys

min_sum = sys.maxsize
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False] * n

def bt(index, start, now, visited, sum):
    global min_sum

    if index == n-1:
        if graph[now][start] != 0:
            min_sum = min(min_sum, sum + graph[now][start])

    for next in range(n):
        if graph[now][next] != 0 and not visited[next] and min_sum > sum:
            visited[next] = True
            bt(index+1, start, next, visited, sum+graph[now][next])
            visited[next] = False

for s in range(n):
    visited[s] = True
    bt(0, s, s, visited, 0)
    visited[s] = False

print(min_sum)