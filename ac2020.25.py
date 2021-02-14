SEED = 1
N = 20201227
SUBJECT_NUMBER = 7

#baby-step giant-step algo discrete log

def loopsize(public):
    start = SEED
    i = 0
    while True:
        start *= SUBJECT_NUMBER
        start %= N
        i += 1
        if start == public:
            return i

def enckey(public, loopsize):
    start = 1
    for i in range(loopsize):
        start *= public
        start %= N
    return start

with open("ac2020.25.txt") as f:
    data = [int(num) for num in f.read().splitlines()]
    publicC = data[0]
    publicD = data[1]

print(enckey(publicD, loopsize(publicC)))
