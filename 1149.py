import sys
input = sys.stdin.readline

# 입력
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# 초기값 설정
# dp[N][Color] = 최소 비용
dp = [[10**6] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = cost[0][i]

# DP 돌리기
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if(j == k):
                continue

            dp[i][j] = min(dp[i][j], dp[i-1][k] + cost[i][j])

print(min(dp[n-1]))