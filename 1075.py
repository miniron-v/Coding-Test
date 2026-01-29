n = int(input())
f = int(input())

n = (n // 100) * 100
mod = n % f
print(f"{((f - mod) % f):02d}")