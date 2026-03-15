import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())

a -= 1
b -= 1

q = deque()
q.append((a, 0))
memo = set()

while q:
    i, c = q.popleft()

    if i == b:
        print(c)
        exit()

    memo.add(i)

    l, r = i, i
    while r + s[i] < n:
        r += s[i]
        if r in memo:
            continue

        q.append((r, c + 1))

    while 0 <= l - s[i]:
        l -= s[i]
        if l in memo:
            continue

        q.append((l, c + 1))

print(-1)