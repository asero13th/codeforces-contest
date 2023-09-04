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

    if n == 1:
        return 0
    i, j = 0, n - 1
    pre, post = 0,0
    ans = 0
    while i <= j:
      
        if pre <= post:
            pre += nums[i]
            i += 1
      
        else:
            post += nums[j]
            j -= 1
        
        if pre == post:
            bob = i - 1
            alice = n - j 

            ans = bob + alice
            
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
