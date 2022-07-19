
n = int(input())
command = list(input().split())
dd = {'R':(1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}

x, y = 1, 1
for c in command:
    dx, dy = dd[c]
    nx = x + dx
    ny = y + dy
    if 0<nx<=n and 0<ny<=n:
        x = nx
        y = ny

print(y, x)