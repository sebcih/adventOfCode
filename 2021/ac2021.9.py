# should have went with connected graph repr.
# Always be careful with your naming, esp in 2d and  more d arrays.
# Honest I should just write a generic bfs func

from collections import deque
from math import prod

def neighbors(board, row, col):
    return [(row + i, col + j, board[row + i][col + j]) for i in range(-1, 2 ,1) for j in range(-1, 2, 1) 
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and abs(i) != abs(j)]

def low_points(board):
    return [(i, j, val) for i, row in enumerate(board) for j, val in enumerate(row) if all(map(lambda n: val < n[2], neighbors(board, i, j)))]

def p1(board):
    return sum(low_point[2] + 1 for low_point in low_points(board))

with open("ac2021.9.txt") as f:
    board = [[int(n) for n in list(line)] for line in f.read().splitlines()]


def bfs(board, p, markeds):
    q = deque()
    q.append(p)
    current = set()
    while q:
        top = q.pop()
        print(top)
        markeds.add(top)
        current.add(top)
        for n in neighbors(board, top[0], top[1]):
            if n not in markeds and n[2] > top[2] and n[2] != 9:
                print(n)
                q.append(n)
    return current
    

def p2(board):
    lps = low_points(board)
    ans = []
    seens = set()
    for p in lps:
        s = bfs(board, p, seens)
        ans.append(s)
        seens |= s
    return prod(sorted(map(len, ans), reverse = True)[:3])
      

print(p2(board))
