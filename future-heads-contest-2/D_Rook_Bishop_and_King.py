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
    r1, c1, r2, c2 = inlt()
    rock, bishop, king = 0,0,0

    if (r1 == r2) or (c1 == c2):
        rock = 1
    else:
        rock = 2

    
    def inbound(x, y):
        return 1 <= x <= 8 and 1 <= y <= 8
    
    visited = set()
    direction = [(1,1), (1,-1),(-1,1),(-1,-1)]
      
    def dfs(a, b,r2,c2):
        nonlocal bishop
        for x, y in direction:
            if  a + x == r2 and b + y == c2:
                if (r1 + c1) == (r2 + c2) or (r1 - c1) == (r2 - c2):
                    bishop = 1
                else:
                    bishop = 2
                
            if inbound(a + x, b + y) and (a + x, b + y) not in visited :
                visited.add((a + x, b + y))
                dfs(a + x, b + y,r2,c2)

    dfs(r1,c1,r2,c2)
    direction2 = [(1,1), (1,-1),(-1,1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)]

    def bfs(r1,c1,r2,c2):
        queue = deque()
        queue.append((r1, c1))
        level = 0
        nonlocal king
        while queue:
            
            for i in range(len(queue)):
                x , y = queue.popleft()
                if x  == r2 and y == c2:
                        king  = level
                        return
                
                for i, j in direction2:
                    
                    if inbound(x + i, y + j):
                        queue.append((x + i, y + j))

            level += 1
    bfs(r1,c1,r2,c2)
    return rock, bishop, king


if __name__ == "__main__":
    print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
