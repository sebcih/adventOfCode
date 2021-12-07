#maybe ranges to save length

def crap_rotate(cups, moves):    
    _max = len(cups) - 1
    start = data[0]
    for i in range(moves):
        picked = get_picked(start, cups)
        dest = start - 1
        while dest in picked or dest < _min:
            dest = (dest - 1) if (dest - 1) >= _min else _max
        cut_picked(cups, picked, start)
        append_after(cups, dest, picked)
        start = cups[start]

def get_picked(start, cups):
    picked = []
    for i in range(3):
        picked.append(cups[start])
        start = cups[start]
    return picked

def cut_picked(cups, picked, start):
    cups[start] = cups[picked[-1]]

def append_after(cups, dest, picked):
    cups[picked[-1]] = cups[dest]
    cups[dest] = picked[0]

def add_extras(cups, limit):
    _max = len(cups) - 1
    cups[data[-1]] = _max + 1
    cups.extend([(i + 1) for i in range(_max + 1, limit)])
    cups.append(data[0])

def init_cups(data):
    cups = [0] * (len(data) + 1) #1 based indexing with self referant zero    
    for i, value in enumerate(data):
        cups[value] = data[(i + 1) % len(data)]
    return cups

def p1():
    crap_rotate(cups, 100)
    ans = ""
    start = 1
    while cups[start] != 1:
        ans += str(cups[start])
        start = cups[start]
    return ans

def p2():
    add_extras(cups, 1000000)
    crap_rotate(cups, 10000000)
    return cups[1] * cups[cups[1]]
        
with open("ac2020.23.txt") as f:
    data = [int(x) for x in f.read().splitlines()[0]]
    _min = min(data)

cups = init_cups(data)
print(p1())
cups = init_cups(data)
print(p2())
