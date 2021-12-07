from functools import reduce

def p1(state, command):
    if command[0] == "forward":
        state = (state[0] + command[1], state[1])
    elif command[0] == "up":
        state = (state[0], state[1] - command[1])
    else:
        state = (state[0], state[1] + command[1])
    return state

def p2(state, command):
    if command[0] == "forward":
        state = (state[0] + command[1], state[1] + command[1] * state[2], state[2])
    elif command[0] == "up":
        state = (state[0], state[1], state[2] - command[1],)
    else:
        state = (state[0], state[1], state[2] + command[1])
    return state
    
        
with open("ac2021.2.txt") as f:
    nums = [(x, int(y[0])) for x, y, *_ in [line.split() for line in f.read().splitlines()]]
    print(final_state := reduce(p1, nums, (0,0)), final_state[0] * final_state[1])
    print(final_state := reduce(p2, nums, (0,0,0)), final_state[0] * final_state[1])




        
