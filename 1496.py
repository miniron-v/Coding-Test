n = int(input())
v = list(map(int, input().split()))
total = sum(v)

memo = {}

# solve(시작 인덱스, 배열 길이) = 최대 차이
def solve(s, l):
    if l <= 0:
        return 0
    if (s, l) in memo:
        return memo[(s, l)]
    
    r = 0
    for i in range(l):
        c = (s + i) % n
        # 내가 획득한 점수에서, 상대가 벌려둔 차이만큼 뺀다.
        d = v[c] - (solve(s, i) + solve((c + 1) % n, l - i - 1))
        r = max(r, d)

    memo[(s, l)] = r
    return r

result = 0
for s in range(n):
    # 선형으로 이어진 새 배열 생성
    diff = v[s] - solve(s + 1, n - 1)
    result = max(result, (total + diff) // 2)

print(result)