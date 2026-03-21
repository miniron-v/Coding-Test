n = int(input())
c = list(map(int, input().split()))

dp = [0] * (max(c) + 1)

for i in c:
    dp[i] += 1

for i in range(max(c), -1, -1):
    if i == dp[i]:
        print(i)
        exit()

print(-1)