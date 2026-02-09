t = int(input())

chance = [[7],
          [2, 4],
          [1, 3, 5],
          [2, 6],
          [1, 5, 7],
          [2, 4, 6, 8],
          [3, 5, 9],
          [4, 8, 0],
          [5, 7, 9],
          [6, 8]]

# dp[N][마지막 수]
dp = [ [0] * 10 for _ in range(1002) ]

dp[1] = [1] * 10

for i in range(1, 1001):
        for prev in range(10):
            if dp[i][prev] == 0:
                 continue
            
            for next in chance[prev]:
                dp[i+1][next] += dp[i][prev]
                dp[i+1][next] %= 1234567

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1234567)

