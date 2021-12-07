from functools import reduce

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n  # try diophantaine equation, sympy and julia and brute force method and understand egcd
    gcd = b
    return x, y

def bezout_reduction(x, y):
    x_base, x_cong = x[0], x[1]
    y_base, y_cong = y[0], y[1]
    x_m, y_m = egcd(x_base, y_base)
    rem = (x_m * x_base * y_cong) + (y_m * y_base * x_cong)
    base = x_base * y_base
    rem += base
    return(base, rem)

with open("ac2020.13.txt") as f:
    data = f.read().splitlines()
    earlist = int(data[0])
    schedule = [(int(v), i) for i, v in enumerate(data[1].split(',')) if v != "x"]
    p1 = min([((v - earlist % v), v) for v, i in schedule], key = lambda x: x[0])
    print(p1[0] * p1[1])
    schedule = [(v, i % v) for v, i in schedule]
    n, r = (reduce(bezout_reduction, schedule[1:], schedule[0]))
    print(n - (r % n))
