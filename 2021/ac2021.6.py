#This is in-place but I dont like the loop, do it functionally

def advance(fishes):
    temp = fishes[-1]
    for i in range(len(fishes), -1, -1):
        if i == 0:
            fishes[6] += temp
            fishes[8] = temp
        else:
            new_temp = fishes[i - 1]
            fishes[i - 1] = temp
            temp = new_temp
    return fishes

def solve(fishes, n):
    for _ in range(n):
        fishes = advance(fishes)
    return sum(fishes)
       
with open("ac2021.6.txt") as f:
    fishes = [int(num) for num in f.read().split(',')]
    fish_histogram = [0 for _ in range(9)]
    for fish in fishes:
        fish_histogram[fish] += 1

print(solve(fish_histogram, 80))
print(solve(fish_histogram, 256))
