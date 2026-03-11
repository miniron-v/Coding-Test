from collections import deque

n = int(input())
s = input()

lc, sc = 0, 0

count = 0
for c in s:
    if c == 'L':
        lc += 1
    elif c == 'S':
        sc += 1

    elif c == 'R':
        if lc > 0:
            count += 1
            lc -= 1
        else:
            break
    elif c == 'K':
        if sc > 0:
            count += 1
            sc -= 1
        else:
            break

    else:
        count += 1

print(count)