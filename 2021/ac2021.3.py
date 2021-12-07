
def filter(rows, pos, most):
    if len(rows) == 1 or pos == 12:
        return rows
    cols = list(map(list, zip(*rows)))
    counter = Counter(cols[pos]).most_common()[most]
    k = counter[0] if counter[1] != len(rows) / 2 else '1' if most == 0 else '0'
    rows = [row for row in rows if row[pos] == k]
    return filter(rows, pos + 1, most)

def p2(rows):
    oxgen_support = int("".join(filter(rows, 0, 0)), 2)
    scrub = int("".join(filter(rows, 0, -1)), 2)
    return oxgen_support * scrub

def p1(rows):
    cols = list(map(Counter, map(list, zip(*rows))))
    gamma = int("".join(list(map(lambda x: x.most_common()[0][0], cols))), 2)
    epsilon = int("".join(list(map(lambda x: x.most_common()[-1][0], cols))), 2)
    return gamma * epsilon

from collections import Counter
with open("ac2021.3.txt") as f:
    rows = [line for line in f.read().splitlines()]

print(p1(rows))
print(p2(rows))
