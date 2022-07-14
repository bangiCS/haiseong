
dp = [0]

# dp(n-2) : * 2
# dp(n-1) : * 1
# dp(n) = dp(n-1) + 2 * dp(n-2)

n = int(input())

dp.append(1)
dp.append(3)
for i in range(3,n + 1):
    dp.append(dp[i-1] + 2 * dp[i-2])

print(dp[n] % 10007)