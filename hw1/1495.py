
import sys
input = sys.stdin.readline

answer = -1

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
now = s

def bt(index, now):
    global answer
    if index == n:
        answer = max(answer, now)

    elif index<n:
        if 0<= now + v[index] <= m:
            now += v[index]
            bt(index+1, now)
            now -= v[index]

        if 0<= now - v[index] <= m:
            now -= v[index]
            bt(index+1, now)
            now += v[index]

bt(0, s)

print(answer)