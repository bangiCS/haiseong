
from collections import deque

a, b, c = map(int ,input().split())
visited = dict()

if sum([a,b,c]) % 3 != 0:
    print(0)
    exit(0)

def bfs(a,b,c):
    queue = deque([(a,b,c)])
    visited[str(a)+' '+str(b)+' '+str(c)] = True
    solve = False
    while queue:
        a, b, c = queue.popleft()
        # print(a,b,c)
        if a==b==c:
            solve = True
            break

        if a > b:
            if str(a-b)+' '+str(b+b)+' '+str(c) not in visited:
                queue.append((a-b,b+b,c))
                visited[str(a-b)+' '+str(b+b)+' '+str(c)] = True
        elif a < b:
            if str(a+a)+' '+str(b-a)+' '+str(c) not in visited:
                queue.append((a+a,b-a,c))
                visited[str(a+a)+' '+str(b-a)+' '+str(c)] = True

        if b > c:
            if str(a)+' '+str(b-c)+' '+str(c+c) not in visited:
                queue.append((a,b-c,c+c))
                visited[str(a)+' '+str(b-c)+' '+str(c+c)] = True
        elif b < c:
            if str(a)+' '+str(b+b)+' '+str(c-b) not in visited:
                queue.append((a,b+b,c-b))
                visited[str(a)+' '+str(b+b)+' '+str(c-b)] = True

        if a > c:
            if str(a-c)+' '+str(b)+' '+str(c+c) not in visited:
                queue.append((a-c,b,c+c))
                visited[str(a-c)+' '+str(b)+' '+str(c+c)] = True
        elif a < c:
            if str(a+a)+' '+str(b)+' '+str(c-a) not in visited:
                queue.append((a+a,b,c-a))
                visited[str(a+a)+' '+str(b)+' '+str(c-a)] = True

    if solve:
        print(1)
    else:
        print(0)


bfs(a,b,c)