import heapq
from collections import deque
def dijkstra(graph, start):
    distancs = [float("in") for _  in graph]
    distancs[start] = 0
    visited = set()

    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distancs[neighbor]:
                distancs[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distancs

def jkstra(graph, start, i, j):

    visited = set()
    queue = deque([start, i, j])

    while queue:
        
        current_node = queue.popleft()
        visited.add(current_node)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            neighbor = current_node[0]
            if neighbor in visited or not inBound(neighbor[0], neighbor[1], graph) or graph[neighbor[0]][neighbor[1]] == "X":
                continue

            if x == 1:
                neighbor = (neighbor[0], neighbor[1] - 1) 
            elif x == -1:
                neighbor = (neighbor[0], neighbor[1] + 1)

            queue.append(neighbor)
            visited.add(neighbor)
    return len(visited)



def inBound(i, j, graph):
    return 0 <= i < len(graph) and 0 <= j < len(graph[0])


def solve():
    n,m  = list(map(int, input().split()))
    r, c = list(map(int, input().split()))
    x, y = list(map(int, input().split()))


    graph = []
    for _ in range(n):
        graph.append(list(input().split()))
    print(jkstra(graph, (r, c), x - 1, y - 1))
solve()


