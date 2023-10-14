import sys
import threading

input = sys.stdin.readline
from collections import Counter
import itertools
from math import ceil, floor, log
from collections import defaultdict
from collections import deque


#        ---- Input Functions ----      #


def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    nums = inlt()

    ans = 0
    flag = False

    c = Counter(nums)

    ans = sum(nums)
    # print(ans)
    if -1 in c:
        if c[-1] > 1:
            ans += 4
    else:
        ans -= 4import heapq

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

    return ans
   
t = inp()
for i in range(t):
    print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
