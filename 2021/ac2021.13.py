#auto char recognition

with open("ac2021.13.txt") as f:
    coords, rules = f.read().split("\n\n")
    coords = [tuple(int(x) for x in c) for c in [coord.split(",") for coord in coords.splitlines()]]
    rules = [(ins[-1], int(line)) for  ins, line in [rule.split('=') for  rule in rules.splitlines()]]

def pprint(board):
    for row in board:
        print(row)
    
max_height = max(c[1] for c in coords)
max_width = max(c[0] for c in coords)
board = [["." for _ in range(max_width + 1)] for _ in range(max_height + 1)]

def fill_board(board, coords):
    for x, y in coords:
        board[y][x] = "#"

def reflecth(board, line):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if i > line:
                amount = i - line
                new_height = line - amount
                board[new_height][j] = "#" if board[i][j] == "#" else board[new_height][j]
    return [row for i, row in enumerate(board) if i < line] 
    
def reflectv(board, line):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if j > line:
                amount = j - line
                new_width = line - amount
                board[i][new_width] = "#" if board[i][j] == "#" else board[i][new_width]
    return [[col for j, col in enumerate(row) if j < line] for i, row in enumerate(board)]

def score(board):
    return sum(1 for row in board for col in row if col == "#")

def p1(board, rules):  
    for ins, val in rules:
        if ins == "y":
            board = reflecth(board, val)
        else:
            board = reflectv(board, val)
    pprint(board)
    return score(board)
            

fill_board(board, coords)
print(p1(board, rules))
