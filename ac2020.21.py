from itertools import product

def remove_cans(source, targets):
    for target_n, target_d in targets:
        for source_n, source_d in source:
            if target_d in source_d:
                source_d.remove(target_d)

with open("ac2020.21.txt") as f:
    data = [line.split("(contains ") for line in f.read().splitlines()]
    allergens = set()
    ings = set()
    d = [(set(line[0].split()), set(map(lambda x: x.strip(), line[1][:-1].split(",")))) for line in data]
    for key, val in d:
        allergens.update(val)
        ings.update(key)
    ans = []
    for allergen in allergens:
        posses = set(ings)
        for k, v in d:
            if allergen in v:
                posses &= k
        ans.append((allergen, posses))
    mappings = dict()
    while True:
        cans = [(x[0], min(x[1])) for x in ans if  len(x[1]) == 1]
        if not cans:
            break
        mappings.update(dict(cans))
        remove_cans(ans, cans)

    can_contain = set(mappings.values()) | set.union(*(map(lambda x: x[1], ans)))
    cannot_contain = ings - can_contain 
    
    result = 0
    for line in data:
        for word in line[0].split():
            if word in cannot_contain:
                result += 1
    
    print(result)  
    print(",".join([mappings[k] for k in sorted(mappings.keys())]))
