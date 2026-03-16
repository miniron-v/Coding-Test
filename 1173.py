N, m, M, T, R = map(int, input().split())
c, x = 0, m

if m + T > M:
    print(-1)
    exit()

r = 0
while c < N:
    if x + T <= M:
        c += 1
        x += T
    else:
        x = max(m, x - R)
    r += 1

print(r)