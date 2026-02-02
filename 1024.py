def get_first(sum, count):
    return sum // count - (count - 1) // 2

def make_numbers(first, count):
    numbers = range(first, first + count)
    result = ' '.join(map(str, numbers))

    print(result)

# main
n, l = map(int, input().split())

while l * (l - 1) <= 2 * n and l <= 100:
    if l % 2 == 1:
        if n % l == 0:
            make_numbers(get_first(n, l), l)
            break
    else:
        if n % l == l // 2:
            make_numbers(get_first(n, l), l)
            break
    
    l += 1
else:
    print(-1)