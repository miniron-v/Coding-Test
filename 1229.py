# 빠른 풀이 (ajtwlsgmlwn님에게서 아이디어 획득)
n = int(input())

# 육각수 계산
sixnums = []
for i in range(1, n):
    num = 2 * i**2 - i
    if num > n:
        break

    sixnums.append(num)

s = set(sixnums)

# 1, 2, 3, 4인 경우를 모두 전처리
if n in s:
    print(1)
    exit()

for i in sixnums:
    if n - i in s:
        print(2)
        exit()

for i in sixnums:
    for j in sixnums:
        if j >= i:
            break

        if i + j > n:
            break

        if n - i - j in s:
            print(3)
            exit()

if n > 1791:
    print(4)
    exit()

# 그 외는 DP (길어봐야 1790개)
dp = [7] * (n+1)
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    for j in sixnums:
        if j > i:
            break
        
        dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[n])

# 정석 DP
# # 입력
# n = int(input())

# # 육각수 생성 및 DP 초기화
# sixnums = [1]
# dp = [7] * (n + 1)

# s = 1
# while True:
#     # 육각수는 2 * n**2 - n으로도 구할 수 있다.
#     num = sixnums[s-1] + 6 * s + (s-1)**2 - s**2
#     if (num > n):
#         break
    
#     sixnums.append(num)
#     dp[num] = 1
#     s += 1

# dp[0] = 0
# dp[1] = 1
# for i in range(2, n+1):
#     for j in sixnums:
#         if j >= i:
#             break
        
#         dp[i] = min(dp[i], dp[i - j] + 1)

# print(f'dp = {dp}')