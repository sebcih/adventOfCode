from math import sqrt, prod
from collections import defaultdict

#fix this with constraint generator approach
def pp(arr):
    for row in arr:
        print("".join(row))


def convolute(monster, row, col, picture):
    for i in range(monster_height):
        for j in range(monster_width):
            if monster[i][j] == "#":
                if picture[row + i][col + j] != "#":
                    return 0
                    
    for i in range(monster_height):
        for j in range(monster_width):
            if monster[i][j] == "#":
                picture[row + i][col + j] = "O"
    return 1
        
def generate_possiblities(name):
    poss = []
    top, right, bottom, left = reps[name]
    poss.append((0, (top, right, bottom, left))) #identity
    poss.append((1, (right, bottom[::-1], left, top[::-1]))) #90 degrees counterclockwise
    poss.append((2, (bottom[::-1], left[::-1], top[::-1], right[::-1]))) #180 degrees 
    poss.append((3, (left[::-1], top, right[::-1] ,bottom))) #270 degrees counterclockwise 
    poss.append((4, (bottom, right[::-1], top, left[::-1]))) #horizontal flip
    poss.append((5, (top[::-1], left, bottom[::-1], right))) #vertical flip
    poss.append((6, (left, bottom, right, top))) #diagonal flip
    poss.append((7, (right[::-1], top[::-1], left[::-1], bottom[::-1]))) #antidiagonal flip
    return poss

def get_representation(value, num):
    return generate_possiblities(value)[num]

def p1():
    print(prod(corners))

def remove_boarders(array):
    return [row[1:-1] for row in array[1:-1]]

def horizontal_flip(array):
    return [list(row) for row in array[::-1]]

def vertical_flip(array):
    return [list(row[::-1]) for row in array]

def diagonal_flip(array):
    return list(map(list, zip(*array)))

def antidiagonal_flip(array):
    return list(map(lambda x: list(reversed(x)), (zip(*array))))[::-1]  #diagonal #horizontal then vertical flip
    
def rotate_matrix_90_counterclockwise(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]

def apply_transform(array, num):
    if num == 4:
        return horizontal_flip(array)
    elif num == 5:
        return vertical_flip(array)
    elif num == 6:
        return diagonal_flip(array)
    elif num == 7:
        return antidiagonal_flip(array)
    else:
        for i in range(num):
            array = rotate_matrix_90_counterclockwise(array)
    return array

def all_match(need, possibilities):
    for id, edges in possibilities:
        if all((edges[(i)] == e for  i, e in need)):
            return id
    else:
        return -1

def pick_start():
    possible_starts = [(corner, i) for i in range(8) for corner in corners]
    for corner, ori in possible_starts:
        m = {(0,0) : (corner, ori)}
        find_match(0, 1, 0, 0, 3, m)
        find_match(1, 0, 0, 0, 3, m)
        if len(m) == 3:
            return corner, ori
    
def find_match(rowi, coli, prev_rowi, prev_coli, nc, grid):
    candidates = adjs[grid[(prev_rowi, prev_coli)][0]]
    candidates = [c for c in candidates if len(adjs[c]) == nc]
    edges_to_match = [(i, rowi + y, coli + x) for i, (y, x) in enumerate([(1, 0), (0, -1), (-1, 0), (0, 1)]) if (rowi + y, coli + x) in grid]
    m = [(i, get_representation(grid[(y, x)][0], grid[(y, x)][1])[1][i]) for i, y, x in edges_to_match]
    new_m = []
    for i, edge in m:
        mirror = -1
        if i == 0:
            mirror = 2
        elif i == 1:
            mirror = 3
        elif i == 2:
            mirror = 0
        else:
            mirror = 1
        new_m.append((mirror, edge))
    m = new_m
    for c in candidates:
        if (result := all_match(m , generate_possiblities(c))) != -1:
            grid[(rowi, coli)] = (c, result)

with open("monster.txt") as r:
    monster = [[c for c in line] for line in r.read().splitlines()]


with open("ac2020.20.txt") as f:
    data = [line.split(":") for line in f.read().split("\n\n")]
    data = {int(group[0].lstrip("Tile ")): [[c for c in line] for line in group[1].lstrip("\n").splitlines()] for group in data}
    side_len = int(sqrt(len(data)))

reps = {k: ("".join(v[0]), "".join(list(zip(*v))[-1]), "".join(v[-1]), "".join(list(zip(*v))[0]))  for k, v in data.items()}

edges = defaultdict(list)
for id, sides in reps.items():
    for side in sides:
        edges[frozenset((side, side[::-1]))].append(id)
adjs = defaultdict(set)
for _, matches in edges.items():
    if len(matches) == 2:
        matcher = matches[0]
        matchee = matches[1]
        adjs[matchee].add(matcher)
        adjs[matcher].add(matchee)
        
corners = [id for id, ns in adjs.items() if len(ns) == 2]

start_corner, start_ori = pick_start()

grid = {(0,0) : (start_corner, start_ori)}

for rowi in range(side_len):
    for coli in range(side_len):
        if rowi == 0 and coli == 0:
            continue
        if (rowi == side_len - 1 or rowi == 0) and (coli == 0 or coli == side_len - 1):
            if coli == 0:
                find_match(rowi, coli, rowi - 1, coli, 2, grid)
            else:
                find_match(rowi, coli, rowi, coli - 1, 2, grid)
        elif (rowi == side_len - 1 or rowi == 0) or (coli == 0 or coli == side_len - 1):
            if coli == 0:
                find_match(rowi, coli, rowi - 1, coli, 3, grid)
            else:
                find_match(rowi, coli, rowi, coli - 1, 3, grid)     
        else:
            find_match(rowi, coli, rowi, coli - 1, 4, grid)

len_with_borders = len(reps[grid[(0,0)][0]][0])
len_sans_frontiers = len_with_borders - 2

picture = [[0 for _ in range(len_sans_frontiers * side_len)] for _ in range(len_sans_frontiers * side_len)]
for coord, (name, ori) in grid.items():
    canon = remove_boarders(apply_transform(data[name], ori))
    for row in range(len(canon)):
        for col in range(len(canon)):
            picture[(coord[0] * len_sans_frontiers) + row][(coord[1] * len_sans_frontiers) + col] = canon[row][col]

monster_height = len(monster)
monster_width  = len(monster[0])


for t in range(8):
    monster_count = 0
    picture = apply_transform(picture, t)
    for row in range(len(picture) - monster_height):
        for col in range(len(picture[0]) - monster_width):
            monster_count += convolute(monster, row, col, picture)
    if monster_count > 0:
        print(t)
        rough_sea_count = 0
        for row in picture:
            for c in row:
                if c == "#":
                    rough_sea_count += 1
        print(rough_sea_count)
        pp(picture)
