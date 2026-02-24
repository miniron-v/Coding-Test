import sys
input = sys.stdin.readline

# 보유한 캐릭터로 최대 가치를 만들어내는 냅색 문제
# 중요한 값은 증가량이므로, 초기에 증가량 데이터를 만들어둬야 한다.
max_level = int(input())
count = list(map(int, input().split()))
power = list(map(int, input().split()))
max_days = int(input())

# 현재 파워 계산 및 dp에 초기화
max_power = sum(count[i] * power[i] for i in range(max_level))
dp = [max_power] * (max_days + 1)

# 아이템 생성 및 DP 실행
for cur_level in range(max_level - 1):  # 모든 만렙 아닌 캐릭터에 대해서
    # 캐릭터가 없으면 넘어가기
    if count[cur_level] == 0:
        continue

    # 현재 레벨에서 가능한 레벨업 조합을 생성
    items = []
    for delta_level in range(1, max_level - cur_level):   # 아이템 생성
        # 감소하면 고를 이유 없음
        if power[cur_level + delta_level] - power[cur_level] > 0:
            items.append((delta_level, power[cur_level + delta_level] - power[cur_level]))

    # 현재 레벨 아이템들로만 DP 돌리기
    for _ in range(min(count[cur_level], max_days)):    # 해당 레벨의 모든 캐릭터에 대해
        for left_day in range(max_days, 0, -1):         # 남은 날짜에 대해 (날짜가 기준)
            for item_day, item_value in items:          # 레벨업 방법에 대해 DP (캐릭터 1명당 1번만 업데이트)
                if left_day < item_day:
                    break
                dp[left_day] = max(dp[left_day], dp[left_day - item_day] + item_value)

print(dp[max_days])

# ----------------------------------------------------------------------------------
# # 틀린 DP (냅색)
# # 틀린 이유: 한 캐릭터가 1 -> 2, 1 -> 3으로 가는 경우가 중복됨. (1명이 2인분함)
# import sys
# input = sys.stdin.readline

# # 보유한 캐릭터로 최대 가치를 만들어내는 냅색 문제
# # 중요한 값은 증가량이므로, 초기에 증가량 데이터를 만들어둬야 한다.
# n = int(input())
# count = list(map(int, input().split()))
# power = list(map(int, input().split()))
# d = int(input())

# # 아이템 생성
# # i의 레벨업을, (소요 기간, 증가량)으로 묶을 수 있음.
# # 레벨업하면 물건 변하지 않음? -> 한 캐릭터 여러번 레벨업을 하나의 아이템으로 처리해서 문제 X
# # ex. 1 -> 2 -> 3이 아닌, 1 -> 3를 바로 사용했음.
# # 만약 이후 3 -> 4를 해야 했다면, 이미 처음에 1 -> 4를 했을 것
# items = []
# for i in range(n):
#     for j in range(1, n - i):
#         # 캐릭터 숫자만큼 반복 추가. 어차피 D명 이상은 레벨업 못 시킴
#         for _ in range(min(count[i], d)):
#             items.append((j, power[i + j] - power[i]))

# # 현재 파워 계산 및 dp에 초기화
# max_power = sum(count[i] * power[i] for i in range(n))
# dp = [max_power] * (d + 1)
        
# # DP (1차원 냅색)
# for day, delta_power in items:
#     for i in range(d, day - 1, -1):
#         dp[i] = max(dp[i], dp[i - day] + delta_power)

# print(items)
# print(dp)
# print(dp[d])

# ----------------------------------------------------------------------------------
# 틀린 코드: 그리디한 접근 (실패)
# 사유: D가 4일 때, 3일을 써서 100(33.3), 1일을 써서 10(10)만큼 올리는 것보다
# 2일을 써서 60(30)을 2번 올리는 게 더 이득일 수 있음.

# n = int(input())
# char_nums = [0] + list(map(int, input().split()))
# char_powers = [0] + list(map(int, input().split()))
# d = int(input())

# # 초기 값 설정
# # increase[현재 레벨][훈련 일수] = 힘 증가량
# increase = [[0] * (n+1-i) for i in range(n)]

# # i = 현재 레벨
# for i in range(1, n):
#     # j = 훈련 일수
#     for j in range(1, n+1 - i):
#         if i + j > n or j > d:
#             break

#         increase[i][j] = char_powers[i+j] - char_powers[i]

# max_power = sum(char_nums[i] * char_powers[i] for i in range(1, n+1))

# # dp?
# while d > 0:
#     max_increase = 0
#     max_increase_rate = 0
#     max_i = 0
#     max_j = 0

#     for i in range(n):
#         # 렙업 가능한 애가 없으면 다음으로
#         if char_nums[i] <= 0:
#             continue

#         # 제일 이득인 거 찾기
#         for j in range(1, min(n + 1 - i, d + 1)):
#             if increase[i][j] / j > max_increase_rate:
#                 max_increase = increase[i][j]
#                 max_increase_rate = increase[i][j] / j
#                 max_i = i
#                 max_j = j

#     if max_increase < 0 or max_i == 0 or max_j == 0:
#         break

#     max_power += max_increase
#     d -= max_j
#     char_nums[max_i] -= 1
#     char_nums[max_i + max_j] += 1

# print(max_power)