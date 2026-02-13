# 더 효율적인 풀이 (최적화, 역방향 DFS)
n, k = map(int, input().split())

def dfs(n, k):
    if k <= n:
        return n - k
    elif k == 1:
        return 1
    elif k % 2 == 1:
        return min(dfs(n, k+1), dfs(n, k-1)) + 1
    else:
        return min(k - n, dfs(n, k // 2) + 1)
    
print(dfs(n, k))

# BFS를 이용한 풀이 (나의 풀이)
# from queue import Queue

# n, k = map(int, input().split())

# def bfs(n, k):
#     queue = Queue()
#     queue.put((n, 0))

#     visited = [False] * (100_001)

#     while queue.qsize() > 0:
#         node = queue.get()

#         if node[0] < 0 or 100_000 < node[0] or visited[node[0]] == True:
#             continue

#         if node[0] == k:
#             return node[1]
        
#         visited[node[0]] = True
        
#         queue.put((node[0]+1, node[1] + 1))
#         queue.put((node[0]-1, node[1] + 1))
#         queue.put((2 * node[0], node[1] + 1))

# print(bfs(n, k))