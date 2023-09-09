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
    traps = []
    for i in range(n):
        traps.append(inlt())
        
    
    traps.sort()

   
    tmp = traps[-1]
    
    for i in range(n):
        a, b = traps[i]

        if b > (tmp[0] - a + 1) ** 2:
            tmp[0] += b - (tmp[0] - a + 1) ** 2
    return tmp[0] - 1

        
        





        

    
if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
