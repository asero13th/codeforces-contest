import sys
import threading

input = sys.stdin.readline
from collections import Counter
import itertools
from math import ceil, floor, log
from collections import defaultdict
from collections import deque
import heapq


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
    nums = inlt()
    val = min(nums)
    heap = []
    for num in nums:
        heapq.heappush(heap, -1 * num)

   
    for i in range(3):
        maximum = heapq.heappop(heap)
        maximum = -1 * maximum
        
        curr = maximum - val
        if curr < val:
            heapq.heappush(heap, (-1 * val))
            val = curr
            
        if curr !=  0:
            heapq.heappush(heap, (-1 * curr))
    c = Counter(heap)

    if len(c) == 1:
        return "YES"
    return "NO"

if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
