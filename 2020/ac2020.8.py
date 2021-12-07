
def execute(acc, ins_p, ins, val):
    if ins == "jmp":
        return acc, ins_p + val
    elif ins == "nop":
        return acc, ins_p + 1
    else:
        return acc + val, ins_p + 1
     
def run(data, acc, ins_p, seen):
    while ins_p not in seen and ins_p < len(data):
        seen.add(ins_p)
        ins, val = data[ins_p][0], int(data[ins_p][1])
        acc, ins_p = execute(acc, ins_p, ins, val)
    return acc, ins_p

def p1(data):
    acc, _ = run(data, 0, 0, set())
    print(acc)
    
def p2(data):
    main_seen = set()
    branch_seen = set()
    acc, ins_p = 0, 0
    while ins_p not in main_seen:
        main_seen.add(ins_p)
        ins, val = data[ins_p][0], int(data[ins_p][1])
        if ins == "jmp" or ins == "nop":
            b_acc, b_ins_p = execute(acc, ins_p, "jmp" if ins == "nop" else "nop", val)
            b_acc, b_ins_p = run(data, b_acc, b_ins_p, branch_seen)
            if b_ins_p >= len(data):
                print(b_acc)
                break
        acc, ins_p = execute(acc, ins_p, ins, val)   

with open("ac2020.8.txt") as f:
    data = [line.split() for line in f.read().splitlines()]
    p1(data)
    p2(data)
