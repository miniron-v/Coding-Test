# antatica, a, c, i, n, t를 제외한 글자를 추출한다.
# 글자 가르칠 수 있는 개수도 5개를 뺀다.
# r, helo, r, 1개면, r을 고르는 게 아무래도 맞다.
# b, x, d, e, f, g, h, j, k 중 3개를 가르치면 3개겠지.
# 알파벳이 26개밖에 안 되니까, 알파벳 기준으로 돌려도, N 기준으로 돌려도 금방.
# 하지만, 알파벳을 고른다고 모든 단어를 외우는 게 아니다. 단어의 모든 철자를 알아야 그제야 읽는다.
# 이전에 가르친 문자가 포함되어야 하므로, DP도 아니다.
# 조합 전부 돌려보는 것도 미친 짓이겠지.
# rc, rb, rx, ho, he, eo라면.
# r이 3개나 있지만, 전부 읽으려면 4개를 알아야 하고
# 반대로 h, e, o는 각 2개씩이지만, 전부 알면 3개를 읽는다.
# 아무리봐도, 모든 조합 실험 외에 숏컷은 없다. 조합 개수를 출력해볼까?
# 10,400,600개. 실제 등장한 애들로 줄이면, 더 줄일 수도 있다.

# ----------------------------------------------------------------------------------
# 진짜 나이브한 코드
# 로직은 이게 맞고, 최적화 방법이 더 있음. (비트마스킹)
# 그냥 알파벳 크기만큼 배열(비트)을 깔아두고, 체크하면 더 빠름.
# (Python3 / 시간 초과) / (PyPy3 / 3080 ms / 111476 KB)
import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()

# 초기값 세팅
words = []
selected = []
r = 0

# 모든 단어 검사 및 초기 데이터 생성
for _ in range(n):
    word = input().rstrip()[4:-4]
    cantRead = False

    new_word = ''
    new_selected = []
    # 필요한 글자 후보 추가
    for i in word:
        if i in 'acint':
            continue
        
        # 하나라도 acint가 아니면 바로 못 읽는다.
        cantRead = True

        if i not in new_selected:
            new_word += i
            new_selected.append(i)
        if i not in selected:
            selected.append(i)

    # a, c, i, n, t로 못 읽는 단어만 추가 
    if cantRead:
        words.append(new_word)
    else:
        # 읽을 수 있는 건 미리 카운트
        r += 1

result = r

# 로직
for c in combinations(selected, min(k - 5, len(selected))):
    # 모든 조합에 대해
    count = r
    for w in words: # words의 한 단어
        canRead = True
        for i in w: # 단어의 한 글자
            if i not in c:
                canRead = False
                break
        
        # c 조합으로 읽을 수 있으면 카운트
        if canRead:
            count += 1
    
    # 최댓값 갱신
    result = max(result, count)

print(result)