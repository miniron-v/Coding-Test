# 입력
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

# 초기 값 생성
dp = [k + 1] * (nums[-1] * k + 1)
dp[0] = 0

# DP
win = 0
for i in range(1, nums[-1] * k + 2):
    for j in nums:
        # i보다 큰 j론 i를 못 만든다.
        if j > i:
            break

        dp[i] = min(dp[i], dp[i-j] + 1)

    if dp[i] > k:
        win = i
        break


winner = 'holsoon' if win % 2 == 0 else 'jjaksoon'
print(f'{winner} win at {win}')