# (Python3 / 40 ms / 32412 KB)
n = int(input())
count = list(map(int, input().split()))

dp = [-1] * n

for i in range(1, n + 1):
    c = count[i - 1]
    index = 0

    while dp[index] > 0:
        index += 1

    while c > 0:
        index += 1
        if dp[index] == -1:
            c -= 1

    dp[index] = i

print(*dp)