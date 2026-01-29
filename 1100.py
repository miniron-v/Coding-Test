board = [list(input()) for _ in range(8)]

count = 0
index = 0

for i in range(8):
    start = 0 if i % 2 == 0 else 1
    for j in range(start, 8, 2):
        if(board[i][j] == 'F'):
            count += 1

print(count)