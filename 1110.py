num = int(input())
result = num
count = 0

while count == 0 or result != num:
    result = (result % 10) * 10 + ((result // 10 + result % 10) % 10)
    count += 1

print(count)