# Python3 / 40 ms / 34536 KB
import math

a = int(input()) / 100
b = int(input()) / 100

# 초기 값
ps = [2, 3, 5, 7, 11, 13, 17]

def c(k, p):
    return math.comb(18, k) * p**k * (1 - p)**(18 - k)

# 확률 계산
sa = sum(c(k, a) for k in ps)
sb = sum(c(k, b) for k in ps)

print(sa + sb - sa * sb)