# 15분 / (Python3 / 36 ms / 32412 KB)
# 출발점과 도착점, 원의 내부 외부 판정에 관한 문제
# 둘 중 하나만 원의 내부에 있을 때, 반드시 해당 원에 진입/이탈이 발생한다.
import sys
input = sys.stdin.readline

def is_in(x, y, cx, cy, r):
    return (x - cx)**2 + (y - cy)**2 < r**2

# 입력
t = int(input())

# 로직
for _ in range(t):
    sx, sy, dx, dy = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        count += is_in(sx, sy, cx, cy, r) ^ is_in(dx, dy, cx, cy, r)

    print(count)