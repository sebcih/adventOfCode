def calculate_score(board, draws):
    return sum(sum(x for x in row if x not in draws) for row in board)

def isWon(board, draws):
    return any(all(x in draws for x in row) for row in board) or any(all(x in draws for x in col) for col in zip(*board))

def play1(draws, boards):
    seen_draws = set()
    seen_draws.update(draws[:4])
    for number in draws[4:]:
        seen_draws.add(number)
        for board in boards:
            if isWon(board, seen_draws):
                return calculate_score(board, seen_draws) * number

def play2(draws, boards):
    seen_draws = set()
    seen_draws.update(draws[:4])
    for number in draws[4:]:
        print(len(boards))
        seen_draws.add(number)
        if len(boards) == 1:
            return boards.pop()
        winning_boards = []
        for board in boards:
            if isWon(board, seen_draws):
                winning_boards.append(board)
        for board in winning_boards:
            boards.remove(board)

    
    
with open("ac2021.4.txt") as f:
    lines = f.read().splitlines()
    draws = [int(x) for x in lines[0].split(',')]
    boards = set()
    for i in range(2, len(lines[2::]), 6):
        board_chunk = lines[i:i+5]
        board = []
        for line in board_chunk:
            board.append(tuple(int(x) for x in line.split()))
        boards.add(tuple(board))

print(play1(draws, boards))
print(play1(draws, [play2(draws, boards)]))
