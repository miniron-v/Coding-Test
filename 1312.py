a, b, n = map(int, input().split())

for _ in range(n):
    a *= 10
    q = a // b
    a = a % b

print(q % 10)