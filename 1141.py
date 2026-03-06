# (Python3 / 40 ms / 32412 KB)
# distinct하고 정렬하면, 다음 것만 비교하면 된다.
# i번째 단어가 i+1의 접두어라면 걔를 제외.
import sys
input = sys.stdin.readline

# 입력
n = int(input())
s = set()   # set으로 중복 제거

for _ in range(n):
    s.add(input().rstrip())

# 정렬 및 리스트 변환
s = sorted(s)

# 접두사 비교
result = len(s)
for i in range(len(s) - 1):
    # i번째 단어가 i + 1번째 단어에 포함된다면
    if s[i+1].startswith(s[i]):
        result -= 1

print(result)