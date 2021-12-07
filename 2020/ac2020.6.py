from functools import reduce

with open("ac2020.6.txt") as f:
    data = [[set(person) for person in group.splitlines()] for group in f.read().split('\n\n')]

def p1():   
    return sum(map(len, map(lambda group: reduce(set.union, group, group[0]), data)))
    
def p2():  
    return sum(map(len, map(lambda group: reduce(set.intersection, group, group[0]), data)))

print(p1())
print(p2())
