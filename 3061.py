# 더 쉬운 방법 (리스트 제거 가능함;)
t = int(input())
for _ in range(t):
    n = int(input())
    cols = list(map(int, input().split()))

    count = 0
    for i in range(1, n+1):
        j = cols.index(i)
        count += j
        cols.pop(j)
    print(count)

# -----------------------------------------------------------------------------------
# # 버블소트 (Python3 / 1496 ms / 32412 KB)
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     cols = [0] + list(map(int, input().split()))

#     count = 0
#     for i in range(1, n+1):
#         j = cols.index(i)
#         while j > i:
#             tmp = cols[j-1]
#             cols[j-1] = cols[j]
#             cols[j] = tmp
#             j -= 1
#             count += 1

#     return count

# t = int(input())
# for _ in range(t):
#     print(solve())