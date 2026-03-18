n = int(input())
k = int(input())

def is_prime(i):
    for j in range(2, int(i**(1/2)) + 1):
        if i % j == 0:
            return False
    
    return True

dp = [1] * (n + 1)
dp[0] = 0
for i in range(k + 1, n + 1):
    if is_prime(i):
        s = 1
        while i * s <= n: 
            dp[i * s] = 0
            s += 1

print(sum(dp))