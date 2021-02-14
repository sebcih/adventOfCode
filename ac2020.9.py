from functools import reduce
from itertools import accumulate

def two_sum(nums, target):
    for num in nums:
        if target - num != num and target - num in nums:
            return True
    else:
        return False

def contigous_sum(data, target):
    sums = [0] + list(accumulate(data))
    start, end = 0, 2
    while sums[end] - sums[start] != target:
        if sums[end] - sums[start] < target:
            end += 1
        else:
            start += 1
    return(max(data[start : end]) + min(data[start : end]))

with open("ac2020.9.txt") as f:
    data = [int(line) for line in f.read().splitlines()]
    s = set(data[:25])
    for i in range(25, len(data)):
        if not two_sum(s, data[i]):
            print(f"silver: {data[i]}")
            print(f"gold: {contigous_sum(data, data[i])}")
        s.remove(data[i - 25])
        s.add(data[i])
