
from collections import deque

a, b, c = map(int ,input().split())
visited = dict()

if sum([a,b,c]) % 3 != 0:
    print(0)
    exit(0)

def bfs(a,b,c):
    queue = deque([(a,b,c)])
    visited[a][b][c] = True
    solve = False
    while queue:
        a, b, c = queue.popleft()
        # print(a,b,c)
        if a==b==c:
            solve = True
            break

        if a > b:
            if not visited[str(a-b)+' '+str(b+b)+' '+str(c)]:
                queue.append((a-b,b+b,c))
                visited[str(a-b)+' '+str(b+b)+' '+str(c)]
        elif a < b:
            if not visited[str(a+a)+' '+str(b-a)+' '+str(c)]:
                queue.append((a+a,b-a,c))
                visited[str(a+a)+' '+str(b-a)+' '+str(c)]

        if b > c:
            if not visited[str(a)+' '+str(b-c)+' '+str(c+c)]:
                queue.append((a,b-c,c+c))
                visited[str(a)+' '+str(b-c)+' '+str(c+c)]
        elif b < c:
            if not visited[str(a)+' '+str(b+b)+' '+str(c-b)]:
                queue.append((a,b+b,c-b))
                visited[str(a)+' '+str(b+b)+' '+str(c-b)]

        if a > c:
            if not visited[str(a-c)+' '+str(b)+' '+str(c+c)]:
                queue.append((a-c,b,c+c))
                visited[a-c][b][c+c]
                visited[str(a-c)+' '+str(b)+' '+str(c+c)]
        elif a < c:
            if not visited[str(a+a)+' '+str(b)+' '+str(c-a)]:
                queue.append((a+a,b,c-a))
                visited[a+a][b][c-a]
                visited[str(a+a)+' '+str(b)+' '+str(c-a)]

    if solve:
        print(1)
    else:
        print(0)


bfs(a,b,c)