# 입력
n, k = map(int, input().split())
heights = [int(input()) for _ in range(n)]

# dp[선택 여부(비트마스킹)][끝에 선 사람의 인덱스]
dp = [[0] * n for _ in range(1 << n)]

# 초기 값 설정
for i in range(n):
    dp[1 << i][i] = 1

# 모든 비트마스크 순회
for mask in range(1, 1 << n):
    # 비트 확인용
    # print(f'mask {mask:04b}: {dp[mask][::-1]}')

    for i in range(n):
        if not (mask & (1 << i)) or dp[mask][i] == 0:
            continue

        for j in range(n):
            if mask & (1 << j) or abs(heights[i] - heights[j]) <= k:
                continue

            next_mask = mask | (1 << j)
            dp[next_mask][j] += dp[mask][i]

print(sum(dp[(1 << n) - 1]))

# 참고한 코드. DFS-DP + 비트마스킹 압축
# def dfs(i, selected):
#     if selected == ((1 << n) - 1):
#         return 1
    
#     if dp[i][selected] > 0:
#         return dp[i][selected]
    
#     dp[i][selected] = 0
#     for j in range(n):
#         if not (selected & (1 << j)) and abs(heights[i] - heights[j]) > k:
#             dp[i][selected] += dfs(j, selected | (1 << j))
    
#     return dp[i][selected]

# result = 0
# for i in range(n):
#     result += dfs(i, 1 << i) 

# print(result)
