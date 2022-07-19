n, m = map(int, input().split())
y, x, dir = map(int, input().split())
dd = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = graph[:][:]
visited[y][x] = 1
cnt = 0
while True:
    cnt += 1
    for i in range(4):
        dir = (dir+3)%4
        ny = dd[dir][0] + y
        nx = dd[dir][1] + x
        if 0<=ny<n and 0<=x<m:
            if graph[ny][nx] != 1 and not visited[ny][nx]:
                y,x = ny,nx
                visited[y][x] = 1
                break

        if i == 3:
            ny = -dd[dir][0] + y
            nx = -dd[dir][1] + x
            if 0<=ny<n and 0<=x<m:
                if graph[ny][nx] != 1:
                    y,x = ny,nx
                    break
            print(cnt)
            exit(0)

