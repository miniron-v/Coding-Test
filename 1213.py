# (Python3 / 36 ms / 32412 KB)
n = input()

# 입력
char = [0] * 26
for c in n:
    char[ord(c) - ord('A')] += 1

# 검증 및 기본 문자열 생성
odd = ''
result = ''
for i in range(26):
    if char[i] == 0:
        continue

    if char[i] % 2 == 1:
        # 홀수가 2개 이상이면 불가능
        if odd != '':
            print('I\'m Sorry Hansoo')
            exit()

        odd = chr(i + ord('A'))
    
    result += chr(i + ord('A')) * (char[i] // 2)

# 전체 문자열 생성 및 출력
print(result + odd + result[::-1])