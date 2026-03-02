# Python3 / 72 ms / 39096 KB
n = int(input())
nums = list(map(int, input().split()))

# dp[i를 끝번으로 하는 연속합] = 최대 연속합
dp = [0] * n
dp[0] = nums[0]

# DP
# i번 숫자가 마지막일 때 최대인 연속합 = i-1번을 마지막으로 하는 최대 연속합 + i
# 이전까지가 -값이라면, 갖다버리고 새로 시작하는 게 이득
for i in range(n):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])

print(max(dp))