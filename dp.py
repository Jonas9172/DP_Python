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

伐木工答案：
x = int(input())
dp = [each for each in range(0,x+1)]
res = [[each] for each in range(0,x+1)]
for i in range(5,x+1):
    for j in range(1,i//2 + 1):
        if dp[j] * dp[i-j] > dp[i] or (dp[j] * dp[i-j] == dp[i] and len(res[j]) + len(res[i-j]) < len(res[i])):
            dp[i] = dp[j] * dp[i-j]
            res[i].clear()
            res[i].extend(res[j])
            res[i].extend(res[i-j])
    
print(' '.join(list(map(str,sorted(res[x])))))
