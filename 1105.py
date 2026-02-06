import sys
input = sys.stdin.readline

l, r = input().split()

if len(l) != len(r):
    print(0)
    exit()

count = 0
i = 0
while i < len(l) and l[i] == r[i]:
    if l[i] == '8':
        count += 1
    i += 1

print(count)