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
        return nums
    idx = nums.index(n - 1 if nums[0] == n else n)
    if idx == n - 1:
        idx = n

    j = idx - 2
    while j > 0 and nums[j] > nums[0]:
        j -= 1
    
    post = nums[idx:]
    curr = nums[j + 1: idx][::-1]
    pre = nums[:j + 1]
    return post + curr + pre


if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
