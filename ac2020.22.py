from collections import deque
from itertools import islice

#Maybe some way to reuse games?

def score(deck):
    return sum(map(lambda x: (len(deck) - x[0]) * x[1], enumerate(deck)))

def game2(p1, p2, seen):
    i = 0
    while True:
        if (tuple(p1), tuple(p2)) in seen:
            return 1, p1
        seen.add((tuple(p1), tuple(p2)))
        if not p1:
            return 2, p2
        if not p2:
            return 1, p1
        p1card = p1.popleft()
        p2card = p2.popleft()
        if (p1card <= len(p1) and p2card <= len(p2)):
            result, deck = game2(deque(islice(p1, 0, p1card)), deque(islice(p2, 0, p2card)), set())
            if result == 1:
                p1.append(p1card)
                p1.append(p2card)
            else:
                p2.append(p2card)
                p2.append(p1card)
        else:
            if p1card > p2card:
                p1.append(p1card)
                p1.append(p2card)
            else:
                p2.append(p2card)
                p2.append(p1card)
        i += 1

def game1(p1, p2):
    i = 0
    while True:
        if not p1:
            return 2, p2
        if not p2:
            return 1, p1
        p1card = p1.popleft()
        p2card = p2.popleft()
        if p1card > p2card:
            p1.append(p1card)
            p1.append(p2card)
        else:
            p2.append(p2card)
            p2.append(p1card)
        i += 1

def part1():
    result, deck = game1(p1, p2)
    return score(deck)

def part2():
    result, deck = game2(p1, p2, set())
    return score(deck)

def init_decks(data):
    return (deque(map(int, (data[0].lstrip("Player 1:\n").splitlines()))),
            deque(map(int, data[1].splitlines())))
    
with open("ac2020.22.txt") as f:
    data = f.read().split("\nPlayer 2:\n")

p1, p2 = init_decks(data)
print(part1())
p1, p2 = init_decks(data)
print(part2())
