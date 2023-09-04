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
    #check if the given input array is beautiful in which we can make all positive and the same parity
    n = inp()
    nums = inlt()

    #check if the given input array is beautiful in which we can make all positive and the same parity
    #if not, return NO

    nums.sort()
    if nums[0] < 0:
        return "NO"
    
    if nums[0] % 2 == 1:
        return "YES"
    
    for i in range(1,n):
        if nums[i] % 2 != nums[i-1] % 2:
            return "NO"
    return "YES"



if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
