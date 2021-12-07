from functools import cache

#Main idea behind hex coordinates, maybe a better parser and neighbors

@cache
def neighbors(coords):
    return set(((coords[0] + x, coords[1] + y, coords[2] + z) for x,y, z in [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, +1, 0), (-1, 0, +1), (0, -1, +1)])) 

def parser(input):
    x,y,z = 0,0,0
    i = 0
    while i < len(input):
        if input[i] == "e":
            x, y = x + 1, y - 1         
        elif input[i] == "w":
            x, y = x - 1, y + 1
        elif input[i : i + 2] == "ne":
            x, z = x + 1, z - 1
            i += 1
        elif input[i : i + 2] == "nw":
            y, z = y + 1, z - 1
            i += 1
        elif input[i : i + 2] == "se":
            y, z = y - 1, z + 1
            i += 1
        else:
            x, z = x - 1, z + 1
            i += 1
        i += 1
    return (x,y,z)

def neighbor_count(coord, space):
    return sum((map(lambda coord: coord in space, neighbors(coord))))


def update(space):
    return set(n for coord in space for n in neighbors(coord) if (n in space and 1 <= neighbor_count(n, space) <= 2) or 
                                                                 (n not in space and neighbor_count(n, space) == 2)) 
    
def p1():
    return len(blacks)
 
def p2(blacks):
    for i in range(100):
        blacks = update(blacks)
    return len(blacks)
    
with open("ac2020.24.txt") as f:
    data = [parser(x) for x in f.read().splitlines()]

blacks = set()
for d in data:
    if d not in blacks:
        blacks.add(d)
    else:
        blacks.remove(d)
    
print(p1())
print(p2(blacks))
