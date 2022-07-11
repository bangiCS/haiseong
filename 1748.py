
number = int(input())
num_len = len(str(number))
sum = 0
# 100
# for i in range(1,num_len+1):
#     if i == num_len:
#         for _ in range(number):
#             sum += i
#     else:
#         # print(9 * 10**(i-1))
#         length = 9 * 10 ** (i - 1)
#         # print(i)
#         sum += i * length
#         number-=length


for i in range(1,num_len):
    # print(9 * 10**(i-1))
    length = 9 * 10 ** (i - 1)
    # print(i)
    sum += i * length
    number-=length

sum += num_len*number

print(sum)
