n = int(input())

dp = [0] * 26
for _ in range(n):
    k = input()[0]
    dp[ord(k) - ord('a')] += 1

result = ''
for i in range(26):
    if dp[i] >= 5:
        result += chr(i + ord('a'))

print(result if result != '' else 'PREDAJA')