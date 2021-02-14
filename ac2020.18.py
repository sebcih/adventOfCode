from functools import partial

def evaluate(takes_precedence, tokens): # check recursive descent parsers and implement one and shunting yard algo there is also nice imps in g
    vals = []
    ops = []
    for token in tokens:
        if token == "(":
            ops.append(token)
        elif token == ")":
            top = ops.pop()
            while top != "(":
                b = vals.pop()
                a = vals.pop()
                vals.append(apply(top, a, b))
                top = ops.pop()
        elif token == "+" or token == "*":
            while ops and takes_precedence(ops[-1], token):
                top = ops.pop()
                b = vals.pop()
                a = vals.pop()
                vals.append(apply(top, a, b))
            ops.append(token)
        else:
            vals.append(int(token))
            
    while ops:
        top = ops.pop()
        b = vals.pop()
        a = vals.pop()
        vals.append(apply(top, a, b))
    return vals.pop()

def p2():
    def f(rhs, lhs):
        order = {"*": 1, "+": 2, "(": 0}
        return order[rhs] >= order[lhs]
    return sum(map(partial(evaluate, f), data))

def p1():
    def f(rhs, lhs):
        order = {"*": 1, "+": 1, "(": 0}
        return order[rhs] >= order[lhs]
    return sum(map(partial(evaluate, f), data))

def apply(op, a, b):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        print("This should not happen")
        
with open("ac2020.18.txt") as f:
    data = [''.join((f" {e} " if e in '()' else e for e in line)).split() for line in f.read().splitlines()]
    print(p1())
    print(p2())
