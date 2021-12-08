def p1(numbers):
    return len([comb for  _, output in numbers for comb in output if len(comb) in [2, 3, 4, 7]])
    
#This solve might be doing unnecesary work check if it can be simplified
def solve(line):
    seven = [combo for combo in line if len(combo) == 3][0]
    one = [combo for combo in line if len(combo) == 2][0]
    four = [combo for combo in line if len(combo) == 4][0]
    eight = [combo for combo in line if len(combo) == 7][0]
    top = seven - one
    nine = [combo for combo in line if combo & (top | four) == (top | four) and len(combo) == 6][0]
    bottom = nine - (top | four)
    three = [combo for combo in line if combo & (top | bottom | one) == (top | bottom | one) and len(combo) == 5][0]
    middle = three - (top | bottom | one)
    zero = eight - middle
    six = [combo for combo in line if combo != nine and combo != zero and len(combo) == 6][0]
    top_right = one - six
    bottom_right = one - top_right 
    five = [combo for combo in line if combo == (nine - top_right)][0]
    top_left = nine - three
    two =  eight - (top_left | bottom_right)
    key = {val : i for i , val in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}
    return key   
    
def p2(numbers):
    ans = []
    for input, output in numbers:
        key = solve(input)
        nums = []
        for val in output:
            nums.append(str(key[val]))
        ans.append(int("".join(nums)))
    return sum(ans)
            
with open("ac2021.8.txt") as f:
    numbers = [(list(map(frozenset, x.split())), list(map(frozenset, y.split()))) for x, y in [line.split(" | ") for line in f.read().splitlines()]]

print(p1(numbers))
print(p2(numbers))
