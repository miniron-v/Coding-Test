n, k = map(int, input().split())
weight, value = 0, 1
stuffs = [list(map(int, input().split())) for _ in range(n)]

# dp[물건 번호][남은 무게]
dp = [[0] * (k + 1) for _ in range(n)]

# 초기값 설정 (첫번째 물건 열 채우기)
for remain_weight in range(k + 1):
    if remain_weight >= stuffs[0][weight]:
        dp[0][remain_weight] = stuffs[0][value]

# DP
for i in range(1, n):
    for remain_weight in range(k + 1):
        # 무게 초과로 못 넣는 경우
        if remain_weight < stuffs[i][weight]:
            dp[i][remain_weight] = dp[i - 1][remain_weight]
            continue

        dp[i][remain_weight] = max(dp[i - 1][remain_weight], dp[i - 1][remain_weight - stuffs[i][weight]] + stuffs[i][value])

print(dp[n-1][k])