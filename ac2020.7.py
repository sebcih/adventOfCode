from functools import reduce

def p1_helper(root, tree, visited):
    visited.add(root)
    if root in tree:
        for child in tree[root]:
            if child not in visited:
                p1_helper(child, tree, visited)

def p1():
    visited_nodes = set()
    p1_helper("shiny gold", contained_by, visited_nodes)
    return len(visited_nodes) - 1

def p2_helper(root, tree):
    if not tree[root]:
        return 1
    else:
        return 1 + reduce(lambda x, y: x + y, [v * p2_helper(k, tree) for k, v in tree[root].items()], 0)

def p2():
    return p2_helper("shiny gold", contains) - 1
        
with open("ac2020.7.txt") as f:
    data = f.read().splitlines()
    contains = {}
    contained_by = {}
    for item in data:
        container, containeds, *_ = item.split(" bags contain ")
        count_dict = {}
        for contained in containeds.split(","):
            count, *color, _ = contained.split()
            if count == "no":
                continue
            contained = color[0] + " " + color[1]
            if contained not in contained_by:
                contained_by[contained] = [container]
            else:
                contained_by[contained].append(container)
            count_dict[contained] = int(count)
        contains[container] = count_dict
        
print(p1())
print(p2())
