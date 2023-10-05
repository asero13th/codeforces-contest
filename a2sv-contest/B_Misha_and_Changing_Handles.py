from collections import defaultdict

n = int(input())
names = defaultdict(list)
hasParent = set()
for _ in range(n):
    old, new = input().split()
    names[old].append(new)
    hasParent.add(new)
print(names)
def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        if node not in visited and node in graph:
            for neigh in graph[node]:
                stack.append(neigh)
                
            
            
    return visited

for name in names:
    if name not in hasParent:
        dfs(name, names)
        # print(dfs(name, names))
