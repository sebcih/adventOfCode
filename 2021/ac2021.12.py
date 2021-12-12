#this screams dynamcic programming

from collections import defaultdict

with open("ac2021.12.txt") as f:
    edges = [line.split("-") for line in f.read().splitlines()]

def make_graph(edges):
    g = defaultdict(list)
    for start, end in edges:
        if start == 'start' or end == 'end':
            g[start].append(end)
        else:
            g[start].append(end)
            g[end].append(start)
    small_caves = {cave for cave in g.keys() if cave.islower()}
    return g, small_caves

def can_add1(cave, path):
    return cave.isupper() or cave not in path

def can_add2(cave, path):
    if cave == "start":
        return False
    counts = {cave : path.count(cave) for cave in small_caves if path.count(cave) > 1}
    return cave.isupper() or len(counts) < 2 and (all(count < 3 for count in counts.values()))

def dfs(g, start, path, paths):
    path = path + (',' + start)
    if start == 'end':
        paths.append(path)
        return
    for n in g[start]:
        if can_add2(n, path):
            dfs(g, n, path, paths)
    
paths = []
graph, small_caves = make_graph(edges)
dfs(graph, "start", "", paths)
print(paths)
print(len(paths))

        
    
