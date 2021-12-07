def p2(data):
    a = 1 if 1 in data else 0
    b = a + 1 if 2 in data else 0
    c = a + b + 1 if 3 in data else 0
    for i in range(4, max(data) + 1):
       a, b, c = b, c, a + b + c if i in data else 0
    return c
                  
def p1(data):
    path = [0] + [i for i in range(1, max(data) + 1) if i in data] + [max(data) + 3]
    diffs = [x - y for x, y in zip(path[1:], path[:-1])]
    return sum((x == 1 for x in diffs)) * sum((x == 3 for x in diffs))
        
with open("ac2020.10.txt") as f:
    data =set(int(line) for line in f.read().splitlines())
    print(p1(data))
    print(p2(data))
