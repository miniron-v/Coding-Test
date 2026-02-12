# 파이썬은 이분 탐색을 지원해준다.
import bisect

# 입력 및 초기값 설정
n = int(input())
nums = list(map(int, input().split()))

# dp[i] = 길이가 i인 증가하는 부분 수열의 마지막 원소
dp = [nums[0]]

# 앞에서부터 하나씩 꺼내본다. i를 쓴다면 첫번째 탐색은 건너뛸 수 있다.
for num in nums:
    # 배열의 맨 끝보다 큰 경우 (기존 LIS 뒤에 붙는 경우)
    if num > dp[-1]:
        dp.append(num)
    # 이분 탐색 결과이므로, num은 항상 dp[pos]보다 작다.
    else:
        dp[bisect.bisect_left(dp, num)] = num

# dp가 곧 가장 긴 증가하는 부분 수열이 되었다.
print(len(dp))