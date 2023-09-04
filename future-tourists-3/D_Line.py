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
    direction = input()
    prefix = []
    
    for i in range(n):
        if direction[i] == "L":
            prefix.append(i)
        if direction[i] == "R":
            prefix.append(n - i)
    
    total = sum(prefix)
    ans = []
    left = n//2
    right = n//2 + 1

    tmp = []
    for i in range(left + 1):
        if direction[i] == "L":
            tmp.append((n - i, i))
    for i in range(right, n):
        if direction[i] == "R":
            tmp.append((i, n -1 - i))
    tmp.sort()
    ans = []
    print(total)
    for val, idx in tmp:
        total = total - prefix[idx] + val
        ans.append(total)
    
    return ans
            
if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
