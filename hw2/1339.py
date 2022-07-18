
cnt = [0] * (ord('Z') + 1)  # 각 문자의 우선순위를 저장

n = int(input())

words = []
for _ in range(n):
    words.append(list(input()))

for word in words:
    w = word[:]
    base = 1
    while w:
        temp = w.pop()  # 일의 자리부터
        cnt[ord(temp)] += base  # cnt에 자릿수를 곱해서 더함
        base*=10

array = []  # (우선순위, 인덱스)의 배열

for i in range(len(cnt)):
    if cnt[i] != 0:
        array.append([cnt[i], i])

array.sort(reverse=True) # 우선순위 내림차순으로 정렬

start = 9
nums = dict()
for a in array:
    nums[chr(a[1])] = start # 문자마다 하나씩 숫자 할당
    start-=1

sum = 0
for word in words:
    w = word[:]
    base = 1
    while w:
        temp = w.pop()
        sum += base * nums[temp]
        base*=10
print(sum)