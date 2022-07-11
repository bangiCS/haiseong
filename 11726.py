
dp = [0]
n = int(input())
# dp(n+2) = dp(n+1) + dp(n)

for i in range(1,n+1):
    if i == 1:
        dp.append(1)
    elif i == 2:
        dp.append(2)
    else:
        dp.append(dp[i-2] + dp[i-1])
print(dp[-1]%10007)