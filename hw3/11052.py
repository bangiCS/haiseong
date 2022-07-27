
n = int(input())
cards = list(map(int, input().split()))

for i in range(1,len(cards)):
    for j in range(i//2+1):
        cards[i] = max(cards[i], cards[i-j-1] + cards[j])

print(cards[-1])