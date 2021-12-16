from functools import lru_cache
from heapq import *

def neighbors(row, col):
    return [(row + i, col + j) for i in range(-1, 2) for j in range(-1, 2) if abs(i) != abs(j) and
             0 <= row + i < len(board) and 0 <= col + j < len(board) and (row + i, col + j)]

def pprint(board):
    for row in board:
        print(row)

def enlarge(board, size):
    big_board = [[-1 for _ in range(len(board[0]) * size)] for _ in range(len(board) * size)]
    for i in range(len(big_board)):
        for j in range(len(big_board[0])):
            big_board[i][j] = ((i // len(board) + j // len(board[0]) + board[i % len(board)][j % len(board)] - 1) % 9) + 1 # Math Trickery
    return big_board
    
with open("ac2021.15.txt") as f:
    board = [[int(x) for x in line] for line in f.read().splitlines()]
    
board = enlarge(board, 5)
dists = [[float('inf')  for _ in range(len(board[0]))] for _ in range(len(board))]
dists[0][0] = 0

def dijkstras():
    q = []
    heappush(q, (dists[0][0], (0 , 0)))
    while q:
        top = heappop(q)
        for i, j in neighbors(top[1][0], top[1][1]):
            alt = board[i][j] + top[0]
            if alt < dists[i][j]:
                dists[i][j] = alt
                heappush(q, (dists[i][j], (i, j)))
                
                
dijkstras() #Look up imps of dijsktra and try to optimize
print(dists[len(board[0]) - 1][len(board) - 1])
