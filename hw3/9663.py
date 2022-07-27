
n = int(input())

graph = [-1] * n

def is_promising(x, n): # x번째줄 n에 퀸을 놓을수 있는지
    for i in range(x):
        if graph[i] == n:
            return False
        if abs(x - i) == abs(graph[i] - n):
            return False

    return True

cnt = 0

def bt(x):
    global cnt

    if x == n:
        cnt+=1
        return

    for i in range(n):
        if is_promising(x, i):
            graph[x] = i
            bt(x+1)

bt(0)
print(cnt)