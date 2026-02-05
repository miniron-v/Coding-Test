l = int(input())
nums = map(int, input().split())
n = int(input())

left = 0
right = 1001

for i in nums:
    if i <= n:
        left = max(i, left)
    if i >= n:
        right = min(i, right)

print(max(0, (n - left) * (right - n) - 1))