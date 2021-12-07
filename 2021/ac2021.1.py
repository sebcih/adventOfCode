def p1(nums):
    return sum(1 for n1, n2 in zip(nums, nums[1:]) if n2 > n1)

def p2(nums):
    a = [sum(truple) for truple in zip(nums, nums[1:], nums[2:])]
    return p1(a)
        
with open("ac2021.1.txt") as f:
    nums = [int(line) for line in  f.readlines()]
    print(p1(nums))
    print(p2(nums))
