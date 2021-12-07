from collections import Counter as C

def p2():
    ans = []
    for line in open("ac2020.2.txt"):
        limits, char, key = line.split()
        ll, ul = map(int, limits.split('-'))
        ch =  char[0]
        ans.append((key[ll - 1] == ch) != (key[ul - 1] == ch))
    return sum(ans)

def p1():
    ans = []
    for line in open("ac2020.2.txt"):
        limits, char, key = line.split()
        ll, ul = map(int, limits.split('-'))
        ch =  char[0]
        ans.append(ll<= C(key)[ch] <= ul)
    return sum(ans)
    
print(p1())
print(p2())
