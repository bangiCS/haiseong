from itertools import combinations

n, c = map(int, input().split())
array = list(input().split())
array.sort()

answer = list(combinations(array,n))
for a in answer:
    cnt1=0
    cnt2=0
    flag = 0
    for i in a:
        if 'a' == i or 'e' == i or 'i' == i or 'o' == i or 'u' == i:
            cnt1+=1
        else:
            cnt2+=1
        if cnt1>=1 and cnt2>=2:
            flag = 1
    if flag == 1:
        for i in a:
            print(i, end='')
        print()