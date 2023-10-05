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
    return list(s[:len(s)])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    performed = inlt()
    ans = []

    d = {
        "U": 1,
        "D" : -1
    }
    
    for i in range(n):
        num, val = input().split()

  
        for word in val:
            
            performed[i] -= d[word]
            if performed[i] < 0:
                performed[i] = 9
            elif performed[i] > 9:
                performed[i] = 0
        ans.append(performed[i])
    return ans









if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
