import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 초기 값 설정
for i in range(n):
    for j in range(m):
        board[i][j] = -1 if board[i][j] == 'H' else int(board[i][j])

dp = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DP 정의
def invalid(x, y):
    return x < 0 or n <= x or y < 0 or m <= y or board[x][y] == -1

def dfs(x, y):
    if invalid(x, y):
        return 0

            
    # 이번 DFS에서 이미 들른 곳이라면 무한 반복 가능 (사이클)
    if visited[x][y] == 1:
        print(-1)
        exit()

    # 이미 값을 구한 곳은 두번 탐색 X
    if dp[x][y] > -1:
        return dp[x][y]
    visited[x][y] = True
    dp[x][y] = 0
    
    # 내 칸의 값 => 내가 앞으로 최대한 움직였을 때 횟수
    for d in range(4):
        nx, ny = x + dx[d] * board[x][y], y + dy[d] * board[x][y]
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    # 다른 DFS에 영향 줄 수 있으니 지우기
    visited[x][y] = False
    return dp[x][y]

# DP 실행 및 출력
print(dfs(0, 0))