
k = int(input())
expression = list(input().split())

numbers = '0123456789'
max_str = list(numbers[::-1][:k+1])
min_str = list(numbers[:k+1])

cnt = 0
i=0
for i in range(len(expression)):
    if expression[i] == '>':
        if cnt != 0:
            max_str = max_str[:i-cnt] + max_str[i-cnt:i+1][::-1] + max_str[i+1:]
        cnt = 0
    elif expression[i] == '<':
        cnt += 1

i+=1
if cnt != 0:
    max_str = max_str[:i - cnt] + max_str[i-cnt:i+1][::-1] + max_str[i + 1:]

for m in max_str:
    print(m,end='')

cnt = 0
i=0
for i in range(len(expression)):
    if expression[i] == '<':
        if cnt != 0:
            min_str = min_str[:i-cnt] + min_str[i-cnt:i+1][::-1] + min_str[i+1:]
        cnt = 0
    elif expression[i] == '>':
        cnt += 1

i+=1
if cnt != 0:
    min_str = min_str[:i - cnt] + min_str[i-cnt:i+1][::-1] + min_str[i + 1:]

print()
for m in min_str:
    print(m,end='')