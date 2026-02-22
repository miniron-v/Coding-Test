# 입력
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

# DP
for i in range(n):
    for j in range(n):
        jump = board[i][j]
        if jump <= 0:
            continue

        print(f'jump = {board[i][j]}')

        if 0 <= i + jump < n:
            dp[i+jump][j] += dp[i][j]
            print(f'dp[{i}][{j}] to dp[{i+jump}][{j}], send {dp[i][j]}')
            
        if 0 <= j + jump < n:
            dp[i][j+jump] += dp[i][j]
            print(f'dp[{i}][{j}] to dp[{i}][{j+jump}], send {dp[i][j]}')
    
print(dp[n-1][n-1])