import sys

n, score, p = map(int, input().split())

if n == 0:
    print(1)
    sys.exit(0)

rank = list(map(int, input().split()))

i = 0
while i < n and rank[i] > score:
    i += 1

print(i + 1 if n < p else i + 1 if score > rank[n-1] else -1)