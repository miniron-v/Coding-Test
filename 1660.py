n = int(input())

# 사면체 생성
tri = 0
tetra = 0

tetras = []
dp = [n] * (n + 1)

# 초기값(사면체) 생성
for i in range(n):
    tri += i
    tetra += tri

    if tetra > n:
        break

    tetras.append(tetra)
    dp[tetra] = 1

# DP (Python3 / 34752 KB / 7680 ms) (PyPy3 / 112920 KB / 204 ms)
for i in range(1, n + 1):
    for j in tetras:
        if j > i:
            break

        dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[n])

# # DP (Python3 / 34752 KB / 7680 ms) (PyPy3 / 112920 KB / 204 ms)
# for i in range(1, n + 1):
#     for j in tetras:
#         if j > i:
#             break

#         dp[i] = min(dp[i], dp[i - j] + 1)

# # DP 바텀업 (Python3 / 시간초과) (PyPy3 / 112920 KB / 344 ms)
# for i in range(1, n + 1):
#     for j in tetras:
#         if i + j > n:
#             break

#         dp[i + j] = min(dp[i + j], dp[i] + 1)
