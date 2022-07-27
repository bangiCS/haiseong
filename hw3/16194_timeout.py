import math

n = int(input())
cards = [0] + list(map(int, input().split()))

answer = 0

while n > 0:
    min_idx = n
    min_sum = cards[n]
    for i in range(1,n):
        if min_sum > math.ceil(n/i) * cards[i]:
            min_sum = math.ceil(n/i) * cards[i]
            min_idx = i
    n = n%min_idx
    answer += min_sum

print(answer)