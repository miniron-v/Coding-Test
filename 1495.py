# (Python3 / 40 ms / 32544 KB)
# Set을 이용한 풀이
# 입력
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
vs = list(map(int, input().split()))

# 초기 값 설정
dp = {s}

# DP
for v in vs:
    if not dp:
        break

    next_dp = set()
    for i in dp:
        if i + v <= m:
            next_dp.add(i + v)
        if i - v >= 0:
            next_dp.add(i - v)

    dp = next_dp

# 출력
print(max(dp) if dp else -1)
# ---------------------------------------------------------------------------------
# # (Python3 / 48 ms / 32412 KB)
# # 1차원 DP를 이용한 풀이 -> 어차피 이전 볼륨 후보만 알면 된다.
# # 입력
# import sys
# input = sys.stdin.readline

# n, s, m = map(int, input().split())
# vs = list(map(int, input().split()))

# # 초기 값 설정
# dp = [-1] * (m + 1)
# dp[s] = s

# # DP
# for v in vs:
#     can_proceed = False

#     next_dp = [-1] * (m + 1)
#     for i in range(m + 1):
#         if dp[i] > -1:
#             if i + v <= m:
#                 next_dp[i + v] = i + v
#                 can_proceed = True
#             if i - v >= 0:
#                 next_dp[i - v] = i - v
#                 can_proceed = True

#     dp = next_dp

#     # 볼륨을 변경하지 못했다면 즉시 종료
#     if can_proceed == False:
#         break

# # 출력
# print(max(dp))
# -------------------------------------------------------------------------------
# # 20분 성공 / (Python3 / 52 ms / 33432 KB)
# # 2차원 DP를 이용한 풀이
# # 입력
# import sys
# input = sys.stdin.readline

# n, s, m = map(int, input().split())
# v = list(map(int, input().split()))

# dp = [[-1] * (m + 1) for _ in range(n + 1)]
# dp[0][s] = s

# # DP
# for i in range(n):
#     can_proceed = False
#     for j in range(m + 1):
#         if dp[i][j] > -1:
#             if j + v[i] <= m:
#                 dp[i+1][j+v[i]] = dp[i][j] + v[i]
#                 can_proceed = True
#             if j - v[i] >= 0:
#                 dp[i+1][j-v[i]] = dp[i][j] - v[i]
#                 can_proceed = True

#     if can_proceed == False:
#         break

# print(max(dp[n]))