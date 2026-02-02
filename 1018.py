def charToInt(c):
    return int(c == 'B')

def countChanged(board):
    white = sum(sum(row) for row in board)
    black = 64 - white

    return min(white, black)

# main
n, m = map(int, input().split())

board = [[(i + j + charToInt(c)) % 2
         for j, c in enumerate(input())]
         for i in range(n)]

minCount = 99
for i in range(n - 7):
    for j in range(m - 7):
        subBoard = [row[j : j + 8] for row in board[i : i + 8]]
        minCount = min(minCount, countChanged(subBoard))

print(minCount)