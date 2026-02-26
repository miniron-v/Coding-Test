# 정렬 후 순차적으로 계산하는 방식. O(n log n + 2n)
# 입력
n, d = map(int, input().split())
shortcut = [tuple(map(int, input().split())) for _ in range(n)]
shortcut.sort(key = lambda x : x[0])    # 시작점 기준 오름차순

# 초기값 설정
dp = [i for i in range(d + 1)]

# DP
for start, end, dist in shortcut:
    # 목적지 넘어가면 스킵
    if end > d:
        continue

    # 지름길 안 써도 되면 스킵
    if dp[start] + dist >= dp[end]:
        continue

    # 지름길 통과 후, 모든 길을 갱신
    dp[end] = dp[start] + dist
    for j in range(1, d - end + 1):
        dp[end + j] = min(dp[end + j], dp[end] + j)

print(dp[d])