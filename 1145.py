from math import lcm
from itertools import combinations

nums = list(map(int, input().split()))
answer = 1000000

for c in combinations(nums, 3):
    answer = min(answer, lcm(c))

print(answer)