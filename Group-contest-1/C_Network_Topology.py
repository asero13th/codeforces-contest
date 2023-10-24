import sys
import threading


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



visited = set()
def solve():
    n, m = inlt()
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = inlt()
        graph[u].append(v)
        graph[v].append(u)

    path = [len(graph[i]) for i in range(1, n + 1)]
    if path.count(1) == 2 and path.count(2) == n - 2:
        return "bus topology"
    elif all(degree == 2 for degree in path):
        return "ring topology"
    elif path.count(1) == n - 1 and path.count(n - 1) == 1:
        return "star topology"
    else:
        return "unknown topology"


if __name__ == "__main__":
    print(solve())
