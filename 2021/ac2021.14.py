from collections import defaultdict
from collections import Counter

with open("ac2021.14.txt") as f:
    start, rules = f.read().split("\n\n")
    rules = [rule.split(' -> ') for rule in rules.splitlines()]
    rules = dict(rules)

def update(pairs, rules):
    new_pairs = defaultdict(int)
    for key in pairs.keys():
        if key in rules:
            new_pairs[key[0] + rules[key]] += pairs[key]
            new_pairs[rules[key] + key[1]] += pairs[key]
    return new_pairs
        

def make_pairs(s):
    pairs = defaultdict(int)
    for i in range(len(s) - 1):
        pairs[s[i:i + 2]] += 1
    return s[0], pairs, s[-1]

def stat(start, pairs, end):
    counts = defaultdict(int)
    counts[start] += 1
    counts[end] += 1
    for (first, second), val in pairs.items():
        counts[first] += val
        counts[second] += val
    return (max(counts.values()) -  min(counts.values())) // 2

def p1(s):
    start, pairs, end = make_pairs(s)
    for i in range(40):
        pairs = update(pairs, rules)
    return stat(start, pairs, end)


print(p1(start))
