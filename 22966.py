n = int(input())

min = 5
result = ""
for _ in range(n):
    arr = list(map(str, input().split()))

    if(int(arr[1]) < min):
        result = arr[0]
        min = int(arr[1])

print(result)