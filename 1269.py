# (Python3 / 192 ms / 70548 KB) / (PyPy3 / 192 ms / 165708 KB)
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

c = len(a)

for i in b:
    c += -1 if i in a else 1

print(c)