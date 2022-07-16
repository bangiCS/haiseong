
n, m = map(int, input().split())
r, c, d = map(int, input().split())
dir = [(-1, 0), (0, 1), (1, 0),(0, -1)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt+= 1

    for i in range(4):
        d = (d+3) % 4
        dr, dc = dir[d]
        if graph[r+dr][c+dc] == 0:
            r+=dr
            c+=dc
            break

        if i==3:
            dr, dc = dir[d]
            if graph[r-dr][c-dc] != 1:
                r-=dr
                c-=dc
                break
            else:
                print(cnt)
                exit(0)
