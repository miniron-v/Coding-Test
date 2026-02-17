import sys
input = sys.stdin.readline

# 입력
sentence = ' ' + input().rstrip('\n')
n = int(input())
words = [input().rstrip('\n') for _ in range(n)]

# 초기값 설정
dp = [51] * len(sentence)
dp[0] = 0

# 더 빠르게 검증
def get_cost(a, b):
    if len(a) != len(b):
        return -1
    
    c = len(a)
    arr_a, arr_b = [0] * 26, [0] * 26

    count = 0
    for i in range(c):
        if a[i] != b[i]:
            count += 1
        
        arr_a[ord(a[i]) - ord('a')] += 1
        arr_b[ord(b[i]) - ord('a')] += 1

    return count if arr_a == arr_b else -1 

# DP
for i in range(1, len(sentence)):
    for word in words:
        k = len(word)
        if i - k < 0:
            continue

        cost = get_cost(sentence[i-k+1:i+1], word)
        if cost == -1:
            continue

        dp[i] = min(dp[i], dp[i - k] + cost)

# 출력
result = -1 if (dp[len(sentence) - 1]) == 51 else dp[len(sentence) - 1]
print(result)

# # 같은 문자인지 검증
# def is_same(a, b):
#     return sorted(a) == sorted(b)
    
# def get_cost(a, b):
#     count = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             count += 1
    
#     return count

# 위 코드 사용한 DP
# for i in range(1, len(sentence)):
#     for word in words:
#         k = len(word)
#         if i - k < 0:
#             continue

#         compare = sentence[i-k+1:i+1]
#         if is_same(compare, word) == False:
#             continue

#         dp[i] = min(dp[i], dp[i - k] + get_cost(compare, word))