def neighbors(board, row, col, flasheds):
    return [(row + i, col + j) for i in range(-1, 2 ,1) for j in range(-1, 2, 1) 
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and (i != 0 or j != 0) and (row + i, col + j,) not in flasheds]

def substep1(board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            board[i][j] += 1

def flashes(board):
    return [(i, j) for i, row in enumerate(board) for j, col in enumerate(row) if col > 9]
            
def flash(board, flasheds, point):
    flasheds.add((point[0], point[1]))
    board[point[0]][point[1]] = 0
    for n in neighbors(board, point[0], point[1], flasheds):
        board[n[0]][n[1]] += 1
        
def step(board):
    substep1(board)
    fs = flashes(board)
    flasheds = set()
    count = 0
    while fs:
        for point in fs:
            count += 1
            flash(board, flasheds, point)
        fs = flashes(board)     
    return board, count
    
    
with open("ac2021.11.txt") as f:
    board = [[int(n) for n in list(line)] for line in f.read().splitlines()]


def p1(board):
    sum = 0
    for _ in range(100):
        board, count = step(board)
        sum += count
    return sum

def p2(board):
    i = 0
    while True:
        board, count = step(board)
        if count == len(board) * len(board[0]):
            return i + 1
        i += 1
            
print(p2(board))
