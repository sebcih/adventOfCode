def update(turn, num, spokens):
    if num in spokens:
        cur_num = turn - spokens[num]
        spokens[num] = turn
        return turn + 1, cur_num, spokens
    else:
        spokens[num] = turn
        return turn + 1, 0, spokens

def game(limit):
    last_num = data[-1]
    turn = len(data)
    nums = {v : i for i, v in enumerate(data[:-1], 1)}
    while turn < limit:
        turn, last_num, nums = update(turn, last_num, nums)
    return last_num

def p1():
    return game(2020)

def p2():
    return game(30000000)
    
with open("ac2020.15.txt") as f:
    data = [int(num) for line in f.read().splitlines() for num in line.split(",")]

print(p1())
print(p2())
