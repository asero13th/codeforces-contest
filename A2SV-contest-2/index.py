import heapq
def longestPalindromeSubstring(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # Single character substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromic substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromic substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]

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

