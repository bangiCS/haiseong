from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int,input().split())
graph = [[-1]*n for _ in range(n)]

queue = deque([(r1,c1)])
graph[r1][c1] = 0
is_solved = False

while queue:
    r, c = queue.popleft()

    if r == r2 and c == c2:
        print(graph[r][c])
        is_solved = True
        break

    for next_r, next_c in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
        if 0<=next_r<n and 0<=next_c<n:
            if graph[next_r][next_c] == -1:
                queue.append((next_r,next_c))
                graph[next_r][next_c] = graph[r][c] + 1

if not is_solved:
    print(-1)