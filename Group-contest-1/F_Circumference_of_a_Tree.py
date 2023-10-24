from collections import deque, defaultdict

def bfs(u, n, adj):
    dist = [-1] * n
    dist[u] = 0
    queue = deque([u])
    while queue:
        v = queue.popleft()
        for to in adj[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                queue.append(to)
    return dist

def find_circumference(n, adj):
    dist = bfs(0, n, adj)
    u = dist.index(max(dist))
    dist = bfs(u, n, adj)
    diameter = max(dist)
    circumference = 3 * diameter
    return circumference

 
n = int(input())
adj = defaultdict(list)
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
    
print(find_circumference(n, adj))

# Usage:
# n = number of nodes
# adj = adjacency list of the tree
# print(find_circumference(n, adj))