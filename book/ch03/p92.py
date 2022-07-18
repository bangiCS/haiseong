
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array.pop()
second = array.pop()

print((m//(k+1) * (first*k + second)) + (m%(k+1) * first))