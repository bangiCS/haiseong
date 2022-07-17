
dp = [0]
dp.append(1)
dp.append(2)
dp.append(4)
for j in range(4, 1000000+ 1):
    dp.append((dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009)

time = int(input())
for i in range(time):
    n = int(input())
    print(dp[n]%1000000009)