# (Python3 / 71968 KB / 1872 ms) (PyPy3 / 118552 KB / 736 ms)
n = int(input())

dp = [1] * (n + 1)

for i in range(2, n + 1):
    k = i - round((2 * i + 1)**(1/2)) + 1
    # 2T(k, r) + T(n - k, r - 1). 기둥 3개인 하노이 탑의 경우의 수는 2**n - 1개다.
    dp[i] = (2 * dp[k] + 2**(i - k) - 1) % 9901

print(dp[n])