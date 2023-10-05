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

    zero = True if nums[0] % 2 == 0 else False
    one = True if nums[1] % 2 == 0 else False

    for i in range(2, n, 2):
        curr = True if nums[i] % 2 == 0 else False
        if curr != zero:
            return "NO"
    for i in range(3, n, 2):
        curr = True if nums[i] % 2 == 0 else False
        if curr != one:
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
