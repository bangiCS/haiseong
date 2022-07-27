import math

n = int(input())
cards = [0] + list(map(int, input().split()))

# for i in range(1,len(cards)):
#     for j in range(i//2+1):
#         cards[i] = min(cards[i], cards[i-j-1] + cards[j])
#
# print(cards[-1])
answer = 0

while n > 0:
    min_idx = n
    min_sum = cards[n]
    for i in range(1,n):
        if min_sum > math.ceil(n/i) * cards[i]:
            min_sum = math.ceil(n/i) * cards[i]
            min_idx = i
    # while n >= min_idx:
    #     n -= min_idx
    n = n%min_idx
    answer += min_sum

print(answer)