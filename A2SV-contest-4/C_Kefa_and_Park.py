from collections import defaultdict, deque

def inlt():
    return list(map(int, input().split()))

def invr():
    return map(int, input().split())

def solve():
    n, m = inlt()
    cats = inlt()
    graph = defaultdict(list)
    for i in range(n - 1):
        x, y  = inlt()
        graph[x].append(y)
        graph[y].append(x)

    visited = set()
    queue = deque()
    queue.append((1, cats[0], 0))
    ans = 0

    while queue:
        
        node, cat, count = queue.pop()
        visited.add(node)

        if not graph[node] or (len(graph[node]) == 1 and graph[node][0] in visited):
            ans += 1
        for child in graph[node]:
            if child not in visited:
                if cats[child - 1]:
                    if cat + 1 <= m:
                        queue.append((child, cat + 1, count + 1))
                else:
                    queue.append((child, 0, count + 1))
    return ans

if __name__ == "__main__":
    print(solve())