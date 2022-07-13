
time = int(input())

for _ in range(time):
    m,n,x,y = map(int,input().split())
    i = x
    j = y
    cnt = 1
    while True:
        cnt+=1
        i = (i + m-1)%m
        j = (j + n-1)%n
        if i==1 and j==1:
            break
        if cnt > m*n:
            break

    if i==1 and j==1:
        print(cnt)
    else:
        print(-1)
