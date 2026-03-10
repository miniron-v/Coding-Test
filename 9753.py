import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
    
p = []
for i in range(100001):
    if is_prime(i):
        p.append(i)

t = int(input())
for _ in range(t):
    k = int(input())
    m = float('inf')

    for i in range(len(p)):
        if i + 1 < len(p) and p[i] * p[i+1] > m:
            break
            
        for j in range(i + 1, len(p)):
            v = p[i] * p[j]
            if v >= k:
                if v < m:
                    m = v
                break

    print(m)