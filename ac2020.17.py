from itertools import product
from functools import cache

RANGE = 1

@cache
def neighbors(coords):
    return set(tuple(map(sum, zip(coords, prod))) for prod in product(range(-RANGE, RANGE + 1), repeat = len(coords)) if any(prod))
    
def neighbor_count(coord, space, counts_cache):
    if coord not in counts_cache:
        result = sum((map(lambda coord: coord in space, neighbors(coord))))
        counts_cache[coord] = result
    return counts_cache[coord]

def update(space, counts_cache):
    return set(n for coord in space for n in neighbors(coord) if (n in space and 2 <= neighbor_count(n, space, counts_cache) <= 3) or 
                                                                 (n not in space and neighbor_count(n, space, counts_cache) == 3)) 
def run(space):
    for i in range(6):
        space = update(space, {})
    return len(space)

def p1():
    return run(set((x, y, 0) for y, row in enumerate(data) for x, val in enumerate(row) if val == "#"))

def p2():
    return run(set((x, y, 0, 0) for y, row in enumerate(data) for x, val in enumerate(row) if val == "#"))

with open("ac2020.17.txt") as f:
    data = [[c for c in line] for line in f.read().splitlines()]
    print(p1())
    print(p2())


