import heapq

def dijkstra(graph, start):
    distancs = [float("inf") for _  in graph]
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