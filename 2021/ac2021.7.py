with open("ac2021.7.txt") as f:
    poses = [int(x) for x in f.read().split(',')]

def p1(i):
    return lambda x: abs(x - i)

def p2(i):
    return lambda x: (abs(x - i) + (x - i) * (x - i)) // 2


def solve(poses, cost_func):
    costs = []
    for i in range(len(poses)):
        costs.append((sum(cost_func(i)(pos) for pos in poses), i))
    return costs

print(min(solve(poses, p1), key = lambda x : x[0]))
print(min(solve(poses, p2), key = lambda x : x[0]))
