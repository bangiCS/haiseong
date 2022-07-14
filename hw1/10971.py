
answer = []
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False] * n

def bt(index, start, now, visited, sum):
    print(visited)
    if index == 3:
        if graph[now][start] != 0:
            answer.append(sum + graph[now][start])
            print(answer)


    for next in range(n):
        if graph[start][next] != 0 and not visited[next]:
            visited[next] = True
            bt(index+1, start, next, visited, sum+graph[now][next])
            visited[next] = False

for s in range(4):
    visited[s] = True
    bt(0, s, s, visited, 0)
    visited[s] = False

print(min(answer))