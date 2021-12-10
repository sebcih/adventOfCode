#Try to make it a  (is_corrupted and complete )general function
from functools import reduce

with open("ac2021.10.txt") as f:
    lines = f.read().splitlines()

pairs = {'>' : '<', '}' : '{', ')' : '(', ']' : '['}
points1 = {'>' : 25137, '}' : 1197, ']' : 57, ')' : 3}
points2 = {'<' : 4, '{' : 3, '[' : 2, '(' : 1}

def is_corrupted(line):
    stack = []
    for symbol in line:
        if symbol in pairs.values():
            stack.append(symbol)
        else:
            top = stack.pop()
            if top == pairs[symbol]:
                continue
            else:
                return points1[symbol]
    else:
        return 0

def complete(line):
    stack = []
    for symbol in line:
        if symbol in pairs.values():
            stack.append(symbol)
        else:
            top = stack.pop()
    stack.reverse()
    return stack
        

def p1(lines):
    return sum(map(is_corrupted, lines))

def p2(lines):
    return sorted(reduce(lambda x, y: x * 5 + points2[y], complete(line), 0) for line in lines if is_corrupted(line) == 0)

def p(lines):
    ans = p2(lines)
    print(ans[len(ans) // 2])
 
p(lines)
# print(p(lines))
