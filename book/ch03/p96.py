
n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(min(map(int, input().split())))

print(max(array))