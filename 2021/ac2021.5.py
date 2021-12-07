#could be done with interval trees. Is digitalization necessarry
def points(line):
    if line[0][0] == line[1][0]:
        return [(line[0][0], x) for x in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1)]
    elif line[0][1] == line[1][1]:
        return [(x, line[0][1]) for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1)]
    else:
        x_sign = 1 if line[0][0] < line[1][0] else -1
        y_sign = 1 if line[0][1] < line[1][1] else -1
        return list(zip(range(line[0][0], line[1][0] + x_sign, x_sign), range(line[0][1], line[1][1] + y_sign, y_sign)))
            
def solve(filtered_lines):
    seens = {}
    for line in filtered_lines:
        for point in points(line):
            if point not in seens:
                seens[point] = 1
            else:
                seens[point] += 1
    return sum(1 for _ , value in seens.items() if value > 1)

def p1(lines):
    filtered_lines = [(p1, p2) for p1, p2 in lines if p1[0] == p2[0] or p1[1] == p2[1]]
    return solve(filtered_lines)

def p2(lines):
    return solve(lines)
    
with open("ac2021.5.txt") as f:
    lines = [(tuple(map(int, p1.split(","))), tuple(map(int, p2.split(',')))) for p1, p2 in [line.split(" -> ") for line in f.read().splitlines()]]
    
print(p1(lines))
print(p2(lines))
