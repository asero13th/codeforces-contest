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
    colors = insr()
   
    adj = defaultdict(list)
    color = defaultdict(str)
    for idx, val in enumerate(nums):
        adj[val].append(idx + 2)
    

    color[len(colors)] = colors[-1]

    def dfs(node):
        
        count = 0
        white = 1 if colors[node - 1] == 'W' else 0
        black = 1 if colors[node - 1] == 'B' else 0

        for child in adj[node]:
            w, b, c = dfs(child)

            white  += w
            black += b
            count += c

            if white == black:
                count += 1

        return white, black, count
    return  dfs(1)[2]


if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
