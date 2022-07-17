from collections import deque

n, m = map(int, input().split())
dd = [(-1,0), (0,1), (1,0),(0,-1)]

answer = []
graph1 = []
graph2 = []
for _ in range(n):
    temp = input()
    temp = list(map(int, temp))
    graph1.append(temp[:])
    graph2.append(temp[:])

def bfs(graph, start, start_dis):
    queue = deque([start])
    graph[start[0]][start[1]] = start_dis

    while queue:
        now_y, now_x = queue.popleft()
        for dy,dx in dd:
            if 0<=now_y+dy<n and 0<=now_x+dx<m:
                if graph[now_y+dy][now_x+dx] == 0:
                    graph[now_y + dy][now_x + dx] = graph[now_y][now_x] - 1
                    queue.append([now_y + dy,now_x + dx])

bfs(graph1, [0,0], -1)
if graph1[-1][-1] != 0:
    answer.append(-1 * graph1[-1][-1])
bfs(graph2, [n-1,m-1], -1)

for i in range(n-2):
    for j in range(m):
        if graph1[i][j] < 0 and graph1[i+1][j] == 1:
            if graph2[i+1][j] == 1 and graph2[i+2][j] < 0:
                answer.append(-1*sum([-1,graph1[i][j], graph2[i+2][j]]))
for i in range(n):
    for j in range(m-2):
        if graph1[i][j] < 0 and graph1[i][j+1] == 1:
            if graph2[i][j+1] == 1 and graph2[i][j+2] < 0:
                answer.append(-1*sum([-1,graph1[i][j],graph2[i][j+2]]))

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))



