from functools import reduce

def p1(cur, ins):
    a, v = ins
    curN, curE, dir = cur
    face = dirs[dir]
    if a == "F":
        if face == "N":
            curN += v
        elif face == "S":
            curN -= v
        elif face == "E":
            curE += v
        else:
            curE -= v
    elif a == "N":
        curN += v
    elif a == "S":
        curN -= v
    elif a == "E":
        curE += v
    elif a == "W":
        curE -= v
    elif a == "R":
        dir = (dir + v // 90) % 4
    else:
        dir = (dir + (4 - (v // 90))) % 4
    return (curN, curE, dir)

def p2(cur, ins):
    a, v = ins
    curN, curE, wayN, wayE = cur
    if a == "F":
        curN += v * wayN
        curE += v * wayE
    elif a == "N":
        wayN += v
    elif a == "S":
        wayN -= v
    elif a == "E":
        wayE += v
    elif a == "W":
        wayE -= v
    elif a == "R":
        for i in range(v // 90):
            wayN, wayE = -wayE, wayN
    else:
        for i in range(4 - (v // 90)):
            wayN, wayE = -wayE, wayN
    return(curN, curE, wayN, wayE)
    
def ans(x):
    return abs(x[0]) + abs(x[1])
    

with open("ac2020.12.txt") as f:
    data = [(line[0], int(line[1:])) for line in f.read().splitlines()]
    dirs = ["E", "S", "W", "N"]
    print(ans(reduce(p1, data, (0, 0 ,0))))
    print(ans(reduce(p2, data, (0, 0, 1, 10))))
