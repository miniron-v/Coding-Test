# 각 주사위는 최대 1면, 2면, 3면이 보인다.
# 전체 주사위 묶음에서, 1, 2, 3면 보이는 게 각각 몇 개인지 계산하고, 곱해서 답을 낸다.
# 예외적으로, 1개가 나오면 최댓값만 제외한다.

# Python3 / 36 ms / 32412 KB
from itertools import combinations

n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    print(sum(dice) - max(dice))
    exit()

c1 = (n - 2) * (5 * n - 6) # 가운데 면 + 맨 밑 줄 모서리 라인, (n - 2)**2 * 5 + (n - 2) * 4 
c2 = n * 8 - 12  # 각 모서리 + 밑면 꼭짓점, (n - 2) * 8 + 4
c3 = 4  # 윗면 네 꼭짓점

# m1 = 1면이 보이는 주사위의 최솟값
m1 = min(dice)
m2 = 101
m3 = 151

# m2 계산
for a, b in combinations(range(6), 2):
    # 마주보는 면 제외
    if a + b == 5:
        continue

    m2 = min(m2, dice[a] + dice[b])

# 3면이 보이는 경우의 수
p3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]

# m3 계산
for a, b, c in p3:
    m3 = min(m3, dice[a] + dice[b] + dice[c])

print(c1 * m1 + c2 * m2 + c3 * m3)