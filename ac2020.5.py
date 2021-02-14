ans = []
with open("ac2020.5.txt", 'r') as f:
    for line in f:
        row, col = int(line[:7].replace('F', '0').replace('B', '1'), 2),  int(line[7:].replace('L', '0').replace('R', '1'), 2)
        ans.append(row * 8 + col)
    
def p1():
    return max(ans)

def p2():
    s = set(ans)
    for i in range(p1()):
        if i not in s and i - 1 in s and i + 1 in s:
            return i

print(p1())
print(p2())
