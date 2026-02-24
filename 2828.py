n, m = map(int, input().split())
j = int(input())

d = 0
cur = 1
m -= 1
for _ in range(j):
    a = int(input())

    if cur <= a <= cur + m:
        continue
    
    a = a - m if cur < a else a
    d += abs(a - cur)
    cur = a

print(d)