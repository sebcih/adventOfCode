from functools import reduce

#bitmaps
def parser(line): #can use regular exp here
    task, adrress = line.split('=')
    if task[:-1] == "mask":
        return (task[:-1], adrress[1:])
    else:
        return("mem", int(task[4:-2]), int(adrress[1:]))

def possible_addrs(val):
    addrs = [0 ,1] if val[0] == "X" else [int(val[0])]
    for c in val[1:]:
        if c == "X":
            addrs = [(a << 1 | 1, a << 1) for a in addrs]
            addrs = [a for addr in addrs for a in addr]
        else:
            addrs = [a << 1 | int(c) for a in addrs]
    return addrs
        
def decode(mask, addr):
    binary_addr = f"{addr:b}".zfill(len(mask))
    new_addr = [a if m == "0" else m for m, a in zip(mask, binary_addr)]
    return possible_addrs(new_addr)

def p2():
    mem = {}
    mask = ""
    for ins, *args in data:
        if ins == "mask":
            mask = args[0]
        if ins == "mem":
            addr, val = args
            addrs = decode(mask, addr)
            for a in addrs:
                mem[a] = val        
    return(sum(mem.values()))

def p1():
    mem = {}
    mask = ""
    for ins, *args in data:
        if ins == "mask":
            mask = args[0]
        if ins == "mem":
            addr, val = args
            for i, char in enumerate(mask): 
                if char == "1":
                    val |= 1 << (35 - i)
                elif char == "0":
                    val &= ~(1 << (35 - i))
            mem[addr] = val
            
    return(sum(mem.values()))
    
            
with open("ac2020.14.txt") as f:
    data = [parser(line) for line in f.read().splitlines()]
    print(p1())
    print(p2())
