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

def has_cycle(graph,  node, parent):

    
    cycle = False
    TrueTree = True
    stack = [(node, parent)]
    visited.add(node)

    while stack:
        
        current_node, parent_node = stack.pop()
        
     

        for neighbor in graph[current_node]:
            if neighbor in visited and parent_node != neighbor:
                cycle = True
            if len(graph[current_node] ) > 2:
                TrueTree = False
  
            if neighbor not in visited:

                stack.append((neighbor, current_node))
                visited.add(neighbor)

            
    return cycle, TrueTree

visited = set()
def solve():
    n, m = inlt()
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = inlt()
        graph[u].append(v)
        graph[v].append(u)

    answer = 0

    for node in graph:
        if node not in visited:
            cycle, TrueTree = has_cycle(graph, node, -1)
      
            if cycle and TrueTree:
                answer += 1
    return answer
    

if __name__ == "__main__":
    print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
