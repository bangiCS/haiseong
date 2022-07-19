
pos = list(input())
pos[0] = ord(pos[0]) - ord('a')
pos[1] = int(pos[1]) - 1

x,y = pos[0],pos[1]
cnt = 0

for dx,dy in [(-1,-2),(-2,-1),(-1,2),(2,-1),(1,-2),(-2,1),(2,1),(1,2)]:
    nx = dx + x
    ny = dy + y
    if 0<=nx<8 and 0<=ny<8:
        cnt += 1

print(cnt)