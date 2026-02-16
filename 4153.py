while True:
    a, b, c, = map(int, input().split())
    if a == b == c == 0:
        break
    
    if max(a, b, c) == a:
        c, a = a, c

    elif max(a, b, c) == b:
        c, b = b, c

    print('right' if a**2 + b**2 == c**2 else 'wrong')