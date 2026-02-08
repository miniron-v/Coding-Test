import sys
input = sys.stdin.readline

records = input().rstrip('\n')

A, B, C = 0, 1, 2
count = [records.count('A'), records.count('B'), records.count('C')]

# 배열 생성 (크기 할당)
dp = [[[[
    [''] * 3
        for _ in range(3)]
        for _ in range(count[C] + 1)]
        for _ in range(count[B] + 1)]
        for _ in range(count[A] + 1)]

# 초기 값 설정
for prev2 in range(3):
    if count[A] > 0:
        dp[1][0][0][prev2][A] = 'A' 
    if count[B] > 0:
        dp[0][1][0][prev2][B] = 'B'
    if count[C] > 0:
        dp[0][0][1][prev2][C] = 'C'

# DP 실행
for a in range(count[A] + 1):
    for b in range(count[B] + 1):
        for c in range(count[C] + 1):
            for prev2 in range(3):
                for prev1 in range(3):
                    # 이전 순열이 존재하지 않는다면 스킵
                    if dp[a][b][c][prev2][prev1] == '':
                        continue
                    
                    # 1. A 추가 (제약 없음)
                    if a < count[A]:
                        # 마지막 문자가 A가 되니, 끝 글자는 2번째 전 글자가 된다. (prev2, prev1 -> prev1, A)
                        dp[a+1][b][c][prev1][A] = dp[a][b][c][prev2][prev1] + 'A'
                    
                    # 2. B 추가 (끝 글자가 B가 아니어야 함)
                    if b < count[B] and prev1 != B:
                        dp[a][b+1][c][prev1][B] = dp[a][b][c][prev2][prev1] + 'B'
                    
                    # 3. C 추가 (끝 2개 글자가 C가 아니어야 함)
                    if c < count[C] and prev2 != C and prev1 != C:
                        dp[a][b][c+1][prev1][C] = dp[a][b][c][prev2][prev1] + 'C'

def solution():
    # 수많은 dp[A][B][C] 배열 중, 문자열이 존재하면 바로 리턴
    for prev2 in range(3):
        for prev1 in range(3):
            if dp[count[A]][count[B]][count[C]][prev2][j] != '':
                return dp[count[A]][count[B]][count[C]][prev2][prev1]
    # 없으면 -1
    return -1

print(solution())