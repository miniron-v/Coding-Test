import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 초기 값 설정
m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def valid(i, j):
    return 0 <= i < m and 0 <= j < n

# DP
def dfs(i, j):
    if valid(i, j) == False:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if valid(x, y) and maze[i][j] < maze[x][y]:
            dp[i][j] += dfs(x, y)

    return dp[i][j]

print(dfs(m-1, n-1))

# 실패 코드
# for i in range(m):
#     # 위로 전파
#     # for j in range(n):
#     #     if valid(i+1, j) and maze[i-1][j] < maze[i][j]:
#     #         dp[i-1][j] += dp[i][j]

#     # 양 옆으로 전파
#     for j in range(n):
#         if valid(i, j+1) and maze[i][j+1] < maze[i][j]:
#             dp[i][j+1] += dp[i][j]
#     for j in range(n):
#         if valid(i, j-1) and maze[i][j-1] < maze[i][j]:
#             dp[i][j-1] += dp[i][j]

#     # 아래로 전파
#     for j in range(n):
#         if valid(i+1, j) and maze[i+1][j] < maze[i][j]:
#             dp[i+1][j] += dp[i][j]

# print(dp[m-1][n-1])
# print(dp)