# 자릿수를 이용한 덧셈 축약 / (Python3 / 180 ms / 39252 KB) / (PyPy3 / 372 ms / 110812 KB)
a, b = map(int, input().split())

ca = [0] * 10
cb = [0] * 10

while a > 0:
    ca[a % 10] += 1
    a //= 10
    
while b > 0:
    cb[b % 10] += 1
    b //= 10

sum = 0
for i in range(10):
    for j in range(10):
        sum += i * j * ca[i] * cb[j]

print(sum)

# --------------------------------------------------------------------------------
# # 나이브한 방법 (Python3 / 시간 초과) / (PyPy3 / 1880 ms / 110576 KB)
# a, b = input().split()

# sum = 0
# for i in a:
#     for j in b:
#         sum += int(i) * int(j)

# print(sum)