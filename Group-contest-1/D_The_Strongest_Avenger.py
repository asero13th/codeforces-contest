import sys
import threading

from collections import Counter
import itertools
from math import ceil, floor, log
from collections import defaultdict
from collections import deque
from itertools import accumulate

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
    nums = insr()
    nums = list(map(int, nums))


    prefixSum = list(accumulate(nums))
    hashmap = defaultdict(int)
    hashmap[0] = 1

    prefix = 0
    ans = 0
  
    for idx, num in enumerate(prefixSum):
  
        ans += hashmap[num - (idx + 1)]
        hashmap[num - (idx + 1)] += 1


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
