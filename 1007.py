# 점이 2개라면, 경우의 수는 1가지다.
# 점이 4개라면, 1번 점은 2, 3, 4, 3가지로 매칭된다. 나머진 점이 2개므로 1가지. 총 3가지
# 점이 6개라면, 5가지 X 3가지 X 1가지, 총 15가지 경우의 수가 발생한다.
# 점이 20개라면? 19 * 17 * 15 * ... * 1 = 방금 코드 돌려보니 654,729,075개. 타임 아웃이다.
# 메모이제이션이 필요하다.
# 길이가 아니라, 벡터를 구하는 문제다. 접근 방법 자체가 틀릴 수도 있다.
# 만약 반대 방향으로 벡터를 꾸릴 수 있다면? 그만큼 상쇄된다. 각도가 애매학게 틀어지면...
# 그렇다면 내적, 혹은 외적을 쓰는 문제는 아닐까? 아니다. 그건 곱이다.
# 벡터의 합. 여기서 벡터는, 시작과 끝을 잡았을 때, 둘을 뺀 것과 같겠지. 빠진 값이 시작점.
# 그러면 원점을 시작점으로, 끝점을 (끝점 - 시작점)으로 하는 벡터가 된다.
# 원점을 시작점으로 하는 벡터끼리 더한다면, 단순히 두 값을 더하면 된다.
# 즉, 좌표 N개가 주어지면, 그중 절반은 더하고, 절반을 빼서, 그 길이의 최솟값을 구하는 문제다.
# 20개 중 10개를 고르는 연산이므로, 총 184,756개. 이정돈 할만하다.

# 25분 / (Python3 / 시간 초과) / (PyPy3 / 2832 ms / 111252 KB)
from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 입력
    n = int(input())
    dots = []
    for _ in range(n):
        dots.append(tuple(map(int, input().split())))
    
    min_dist = float('inf')
    # 인덱스에서 절반을 선택한 조합에서
    for combs in combinations(range(n), n // 2):
        x, y = 0, 0
        # 선택된 건 더하고 아니면 뺀다.
        for i in range(n):
            if i in combs:
                x += dots[i][0]
                y += dots[i][1]
            else:
                x -= dots[i][0]
                y -= dots[i][1]

        # 제곱된 거리를 저장
        d = x**2 + y**2
        min_dist = min(min_dist, d)

    # 제곱근 씌워서 출력
    print(min_dist**(1/2))