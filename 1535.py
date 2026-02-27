# 9분 성공 / (Python3 / 40 ms / 32412 KB)
# 전형적인 냅색 문제.
# 입력
n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

dp = [0] * 101

# DP
for i in range(n):
    for j in range(100, w[i], -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

# 출력
print(max(dp))