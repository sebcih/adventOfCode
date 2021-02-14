s = set(map(lambda x: int(x), open("ac2020.1.txt")))
TARGET = 2020

def prodsum(target, s):
    for num in s:
        cur_target = target - num
        if cur_target in s and cur_target != num:
            return num * cur_target
    else:
        return 0
            
def p1():
    return prodsum(TARGET, s)

def p2():
    for num in s:
        s.remove(num)
        result = num * prodsum(2020 - num, s)
        if result != 0:
            print(result)
            exit()
        s.add(num)

print(p1())
print(p2())
