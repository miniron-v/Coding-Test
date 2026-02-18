import sys
input = sys.stdin.readline

# 입력
c, n = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]

# 초기 설정
dp = [float('inf')] * (c + 1)
dp[0] = 0

# C명 이상 모으는 DP
for i in range(1, c + 1):
    for j in costs:
        start = max(0, i-j[1])
        m = min(dp[start:i])

        dp[i] = min(dp[i], m + j[0])

# 출력
print(dp[c])