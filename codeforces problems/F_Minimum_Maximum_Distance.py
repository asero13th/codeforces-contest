from collections import defaultdict

def dfs_first_pass(node, parent, distances, marked, tree):
    max_distance = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            max_distance = max(max_distance, dfs_first_pass(neighbor, node, distances, marked, tree) + 1)
    if marked[node]:
        distances[node] = 0
    else:
        distances[node] = max_distance
    return max_distance

def dfs_second_pass(node, parent, distances, marked, tree):
    max_distance = distances[node]
    for neighbor in tree[node]:
        if neighbor != parent:
            max_distance = max(max_distance, dfs_second_pass(neighbor, node, distances, marked, tree) + 1)
    return max_distance

def find_min_fi(n, k, marked_vertices, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    marked = [False] * (n + 1)
    for vertex in marked_vertices:
        marked[vertex] = True

    distances = [0] * (n + 1)
    dfs_first_pass(marked_vertices[0], -1, distances, marked, tree)
    dfs_second_pass(marked_vertices[0], -1, distances, marked, tree)

    min_fi = min(distances)
    return min_fi

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        marked_vertices = list(map(int, input().split()))
        edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
        result = find_min_fi(n, k, marked_vertices, edges)
        print(result)
