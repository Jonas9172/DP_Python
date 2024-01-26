Wonderland答案：

costs = list(map(int, input().split()))
days = list(map(int, input().split()))

lastDay = days[-1]
dp = [0]*(lastDay + 1)

for i in range(1, lastDay+1):
    if i in days:
        option1 = dp[i-1] + costs[0]
        option2 = dp[i-3] + costs[1]
        option3 = dp[i-7] + costs[2]
        option4 = dp[i-30] + costs[3]
        dp[i] = min(option1,option2,option3, option4)
    else:
        dp[i] = dp[i-1]
print(dp[lastDay])
