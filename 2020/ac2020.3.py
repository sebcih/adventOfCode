m = []
for line in open("ac2020.3.txt"):
    m.append(line[:-1])
    
def p1():
    row = 0
    col = 0
    count = 0
    while row < len(m):
        if m[row][col] == "#":
            count += 1
        row += 1
        col = (col + 3) % (len(m[0]))
    return count
    

def p2():
    prod = 1
    for i, j in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        row = 0
        col = 0
        count = 0
        while row < len(m):
            if m[row][col] == "#":
                count += 1
            row += j
            col = (col + i) % (len(m[0]))
        prod *= count
    return prod

print(p1())
print(p2())
