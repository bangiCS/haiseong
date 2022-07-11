
number = int(input())
num_len = len(str(number))
sum = 0

for i in range(1,num_len):
    count = 9 * 10 ** (i - 1)
    sum += i * count
    number-=count

sum += num_len*number

print(sum)
