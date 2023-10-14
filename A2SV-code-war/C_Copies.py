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
    n, x, y = inlt()
    l = 0
    r = n * max(x, y)
    n -= 1
    while l < r:
        mid = (l + r) // 2
        copies = (mid // x) + (mid // y)

        if copies >= n:
            r = mid
        else:
            l = mid + 1
            
    result = l + min(x, y) 
    return result

if __name__ == "__main__":

    print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
