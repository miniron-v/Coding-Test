# (PyPy3 / 104 ms / 110840 KB) / (Python3 / 48 ms / 32412 KB)
# 입력
n, m = map(int, input().split())
k = int(input())
ban = []
for _ in range(k):
    a, b, c, d = map(int, input().split())
    ban.append([(a, b), (c, d)] if a < c or b < d else [(c, d), (a, b)])

# 초기값 설정
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

# DP
for i in range(n + 1):
    for j in range(m + 1):
        if i + 1 <= n and [(i, j), (i + 1, j)] not in ban:
            dp[i + 1][j] += dp[i][j]
            
        if j + 1 <= m and [(i, j), (i, j + 1)] not in ban:
            dp[i][j + 1] += dp[i][j]

print(dp[n][m])