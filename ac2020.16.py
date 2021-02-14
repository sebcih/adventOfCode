from math import prod

def valid(x):
    return any(rule(x) for rule in rules.values())
        
def p1():
    return sum([sum(list(map(lambda field: 0 if valid(field) else field, ticket))) for ticket in tickets]) 

def p2():
    valids = [my_ticket] + [ticket for ticket in tickets if all(map(valid, ticket))]
    possible_ans = {k : set([i for i, field in enumerate(zip(*valids)) if all((v(f) for f in field))]) for k, v in rules.items()}
    sorted_ans = [("", set())] + sorted(possible_ans.items(), key = lambda item: len(item[1]))
    ans = {cur[0]: min(cur[1] - prev[1]) for cur, prev in zip(sorted_ans[1:], sorted_ans[:-1])}           
    return prod([my_ticket[v] for k, v in ans.items() if k.startswith("departure")])
        
with open("ac2020.16.txt") as f:
    data = f.read().split('\n\n')
    rules = {name : rules.split(" or ") for name, rules in map(lambda line: line.split(":"), data[0].splitlines())}
    my_ticket = list(map(int, data[1].splitlines()[1].split(",")))
    tickets = [list(map(int, ticket.split(","))) for ticket in data[2].splitlines()[1:]]
    for k, v in rules.items():
        a = [list(map(int, item.split("-"))) for item in v]
        rules[k] = (lambda a: lambda x: (a[0][0] <= x <= a[0][1]) or (a[1][0] <= x <= a[1][1]))(a)
    
    print(p1())
    print(p2())
