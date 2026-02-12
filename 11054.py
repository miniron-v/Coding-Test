import sys
input = sys.stdin.readline

# 입력
n = int(input())
nums = list(map(int, input().split()))

# DP - 증가하는 수열 구하기
def get_increase_dp(sequence):
    array = [1] * n
    # DP - 증가하는 수열 구하기
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                array[i] = max(array[i], array[j] + 1)

    return array

# i를 마지막 원소로 하는 가장 긴 수열의 길이
dp_increase = get_increase_dp(nums)

# i를 시작 원소로 하는 가장 긴 수열의 길이
dp_decrease = get_increase_dp(nums.reverse())
dp_decrease.reverse()

# i를 중심으로 하는 가장 긴 바이토닉 수열의 길이 구하기
dp = [dp_increase[i] + dp_decrease[i] - 1 for i in range(n)]

print(max(dp))