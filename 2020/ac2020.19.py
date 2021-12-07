#INterpreter maybe, cyk theorem

import re
from functools import cache

RECURSION_DEPTH = 15  

def  lookup(name):
    if name == 8:
        return f"(({lookup(42)})+)"
    elif name == 11:
        return "(" +  "|".join([f"({lookup(42) * i}{lookup(31)* i})" for i in range(1, RECURSION_DEPTH)]) + ")"
    elif name not in environment:
        environment[name] = resolve(rules[name])
    return environment[name]
    
def resolve(exp):
    if isinstance(exp, list) and isinstance(exp[0], str):
        return exp[0]
    elif isinstance(exp, list) and isinstance(exp[0], int):
        return "".join(map(lookup, exp))
    elif isinstance(exp, list) and isinstance(exp[0], list):
        if len(exp) == 1:
            return resolve(exp[0])
        else:
            return f"({resolve(exp[0])}|{resolve(exp[1])})"


with open("ac2020.19.txt") as f:
    data = f.read().split("\n\n")
    rules = [line.split(":") for line in data[0].splitlines()] #TODO: LEARN REGULAR EXP
    rules = {int(line[0]): [[int(s) if s.isdigit() else s.replace("\"", "") for s in sub.split()] for sub in line[1].split("|")] for line in rules if not (int(line[0]) == 8 or int(line[0] == 11))}
    input = data[1].splitlines()
    environment = {}
    prog = re.compile(f"^{lookup(0)}$")
    results = [i for i, line in enumerate(input) if prog.search(line) is not None]
    print(len(results))
