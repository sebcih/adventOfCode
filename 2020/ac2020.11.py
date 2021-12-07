# maybe refactor 2d-map
# a better first maybe

def valid(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])
    
def neighbors(rowi, coli, data):
    return [(rowi + x, coli + y) for y in [-1, 0, 1] for x in [-1, 0, 1] if valid(rowi + x, coli + y) and (x != 0 or y != 0)]

def visible(rowi, coli, data):
    return [result for y in [-1, 0, 1] for x in [-1, 0, 1] if (x != 0 or y != 0) and (result := first(rowi, coli, x, y, data)) != (-1, -1)]

def first(rowi, coli, x, y, data):
    for n in range(1, max(len(data), len(data[0]))):
        xpos = rowi + n * x
        ypos = coli + n * y
        if valid(xpos, ypos):
            if data[xpos][ypos] != ".":
                return (xpos, ypos)
        else:
            break
    return (-1, -1)
                
def count_seats(data):
    return sum(map(lambda row: sum(map(lambda x: x == "#", row)), data))


def rule1(neighbor, m):
    def f(i, j, item):
        if item == "L":
            if all((map(lambda x: m[x[0]][x[1]] != "#", neighbor(i, j, m)))):
                return "#"
            else:
                return item
        else:
            return item            
    return list(list(f(i, j, item) for j, item in enumerate(row)) for i, row in enumerate(m))

def rule2(neighbor, m):
    def f(i, j, item):
        if item == "#":
            if sum((map(lambda x: m[x[0]][x[1]] == "#", neighbor(i, j, m)))) >= 4:
                return "L"
            else:
                return item
        else:
            return item
    return list(list(f(i, j, item) for j, item in enumerate(row)) for i, row in enumerate(m))

def rule22(neighbor, m):
    def f(i, j, item):
        if item == "#":
            if sum((map(lambda x: m[x[0]][x[1]] == "#", neighbor(i, j, m)))) >= 5:
                return "L"
            else:
                return item
        else:
            return item
    return list(list(f(i, j, item) for j, item in enumerate(row)) for i, row in enumerate(m))
  
 
def run_until_stable(r1, r2, neighbors, data):
    prev = 0
    after, new = cycle(r1, r2, neighbors, data)
    while after != prev:
        prev = after
        after, new = cycle(r1, r2, neighbors, new)
        
    return after

def cycle(r1, r2, n, data):
    new = r2(n, r1(n,data))
    return count_seats(new), new

def p1():
    return run_until_stable(rule1, rule2, neighbors, data)

def p2():
    return run_until_stable(rule1, rule22, visible, data)

with open("ac2020.11.txt") as f:
    data = [[c for c in line] for line in f.read().splitlines()]
    print(p1())
    print(p2())
