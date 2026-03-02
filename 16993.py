# 세그먼트 트리 사용, 더 빠른 누적합 구하기
import sys
input = sys.stdin.readline

# total: 전체 합, left: 왼쪽 값 포함 최댓값, right: 오른쪽 값 포함 최댓값, max_sum: 전체 최댓값 (걸쳐질 수 있음)
total, left, right, max_sum = 0, 1, 2, 3

def init(s, e, i):
    if s == e:
        tree[i] = (a[s], a[s], a[s], a[s])
        return tree[i]
    
    m = (s + e) // 2
    L = init(s, m, i * 2)
    R = init(m + 1, e, i * 2 + 1)

    tree[i] = merge(L, R)
    return tree[i]

def merge(L, R):
    t = L[total] + R[total]
    l = max(L[left], L[total] + R[left])
    r = max(R[right], L[right] + R[total])
    m = max(L[max_sum], R[max_sum], L[right] + R[left])
    return t, l, r, m

def query(s, e, i, l, r):
    if l > e or r < s:
        return (0, -float('inf'), -float('inf'), -float('inf'))
    
    if l <= s and e <= r:
        return tree[i]
    
    m = (s + e) // 2
    L = query(s, m, i * 2, l, r)
    R = query(m + 1, e, i * 2 + 1, l, r)

    if L[max_sum] == -float('inf'):
        return R
    if L[max_sum] == -float('inf'):
        return R
    
    return merge(L, R)

n = int(input())
a = list(map(int, input().split()))
m = int(input())

tree = [float('-inf')]  * (n * 4)
init(0, n - 1, 1)

for _ in range(m):
    l, r = map(int, input().split())

    result = query(0, n - 1, 1, l - 1, r - 1)
    print(result[max_sum])

# ---------------------------------------------------------------------------------
# # 단순 누적합 반복 -> 시간 초과 (예상은 했지만 진짜 뜸)
# # 2,000 * 100,000 * K(덧셈, 비교 연산) = 200,000,000 K (제한 시간 2초)
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())

# for _ in range(m):
#     i, j = map(int, input().split())

#     total = -1_000_000_001
#     result = -1_000_000_001
#     for k in range(i - 1, j):
#         total = max(total + a[k], a[k])
#         result = max(result, total)

#     print(result)