import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ban = list(map(int, input().split()))

# 초기 값 설정
dp = [0] * (n + 1)

for i in ban:
    dp[i] = -1

# 막힌 구간을 찾아, 그 앞칸을 목적지로 지정한다.
count = k
for i in range(n, -1, -1):
    if dp[i] == -1:
        count += 1
    else:
        if count >= k:
            n = i
        count = 0

# 목적지는 외치면 이기는 필승 칸이다.
dp[n] = 1

# # dp 돌리면서 채우기
for i in range(n - 1, 0, -1):
    if dp[i] == -1:
        continue

    # 뒤의 k이 모두 패배 칸이면 1(필승 칸)을, 아니면 0(패배 칸)을 기입한다. 
    dp[i] = 1 if all(dp[j] < 1 for j in range(i + 1, min(i + k, n) + 1)) else 0

# 출력
can_win = 0
# 하나라도 필승 칸을 먹을 수 있다면 이긴다.
for i in range(1, min(n, k) + 1):
    if dp[i] == 1:
        can_win = 1
        break

# 출력
print(can_win)

# 아래 방식은 실패한 방법. DP가 아닌 수식과 그리디로 접근한 코드다.
# # dp 돌리기 (가장 작은 필승 수 찾기)
# while 0 < n and dp[n] < 1:
#     print(f'n:{n}')

#     if dp[n] == -1:
#         n -= 1
    
#     else:
#         n -= k + 1

# # 출력
# # print(f'n:{n}')
# # print(dp)
# print(dp[n])