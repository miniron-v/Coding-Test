# 두번째 풀이 방법. 음수는 +와 -가 반복되는 피보나치로 해석 (88352 KB / 324 ms)
# 입력
n = int(input())

# 초기값 설정
is_negative = n < 0
n = abs(n)

dp = [0] * (n+1)
if n != 0:
    dp[1] = 1

# DP 실행
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] % 10**9

# 부호 계산
p = -1 if is_negative and n % 2 == 0 else 1 if n > 0 else 0

# 출력
print(p)
print(dp[n] % 10**9)

# 첫번째 풀이 방법. 로직 그대로 구현한 안전한 방법 (79784 KB / 236 ms)
# # 입력
# n = int(input())

# is_negative = n < 0
# n = abs(n)

# # 초기값 설정
# dp = [0] * (n + 1)

# if n != 0:
#     dp[1] = 1

# # DP 정의
# def positive_fibonacci(n):
#     for i in range(2, n+1):
#         dp[i] = (dp[i-1] + dp[i-2]) % 10**9

#     return dp[n]

# def negative_fibonacci(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1

#     for i in range(2, n+1):
#         dp[i] = dp[i-2] - dp[i-1]
#         dp[i] = abs(dp[i]) % 10**9 * (-1 if dp[i] < 0 else 1)

#     return dp[n]

# # DP 실행
# answer = negative_fibonacci(n) if is_negative else positive_fibonacci(n)
# p = 1 if answer > 0 else -1 if answer < 0 else 0
# answer = abs(answer) % 10**9

# print(p)
# print(abs(answer))