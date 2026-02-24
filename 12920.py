import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

# 전처리
# 중복된 아이템을 개별 처리하면 100 * 10,000 * 10,000 (백 억)번 연산하므로, 무조건 시간 초과
# 따라서 중복된 것들을 묶어서 처리해야 되는데, 이진수를 활용할 수 있음.
# ex. 아이템이 100개 있을 때, 이를 (1, 2, 4, 8, 16, 32)개로 분할 -> 37개가 남음
# 각 아이템은 이진수의 자릿수를 의미. 1개 세트부터 32개 세트까지 전부 더하면 111111(2) = 63
# 남은 것도 묶어서 각각 (1, 2, 4, 8, 16, 32, 37)개를 묶은, 7개의 아이템으로 분할
# 그러면 위 숫자들을 조합해서, 모든 개수의 아이템을 만들어낼 수 있다. (이진수로 생각하면 쉽다.)
# 32까지 써서 만든 숫자(최대 63) + 37로 100까지 모든 숫자 완성 가능.
items = []
for _ in range(n):
    v, c, k = map(int, input().split())
    i = 1   # 이번에 묶을 개수
    while k > 0:
        i = min(i, k)
        items.append((v * i, c * i))    # (무게, 가치)

        k -= i
        i <<= 1
        
# DP (1차원 냅색)
dp = [0] * (m + 1)
for weight, value in items:
    for i in range(m, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[m])