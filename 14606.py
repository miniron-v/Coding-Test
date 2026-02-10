# 입력
n = int(input())

if n < 2:
    print(0)
    exit()

# 초기 값 생성
dp = [0] * (n + 1)
dp[2] = 1

# DP
for i in range(3, n + 1):
    half = i // 2
    dp[i] = (half * (i - half)) + dp[half] + dp[i - half]

# 출력
print(dp[n])