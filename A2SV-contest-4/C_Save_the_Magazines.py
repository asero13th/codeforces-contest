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
    n = inp()
    covers = insr()
    nums = inlt()
    
    ans = 0

    if n < 3:
         nums.sort()
         sum(nums[:nums.count("1") + 1])

    for i in range(2, n):
        n1, n2, n3 = covers[i-2], covers[i-1], covers[i]
        a1,a2,a3 = nums[i-2], nums[i-1], nums[i]

       

        if covers[i - 1] == "1" and a2 <= a1 and covers[i -2] != "1":
            covers[i -2] = "1"
            covers[i - 1] = "0"
        
        if  covers[i] == "1" and a3 <= a2 and  covers[i-1] != "1":
            covers[i] = "0"
            covers[i - 1] = "1"

        if  covers[i] == "1" and covers[i-1] != "1" and a3 <= a1 and  covers[i-2] != "1":
            covers[i] = "0"
            covers[i - 2] = "1"

    for i in range(len(nums)):
        if covers[i] == "1":
            ans += nums[i]
    
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
