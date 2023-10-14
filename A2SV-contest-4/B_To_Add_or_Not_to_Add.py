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
    n, k = inlt()
    nums = inlt()
    nums.sort()
    prefix = 0
    j = 0
    ans = [0, nums[0]]
    for i in range(n):
        prefix += nums[i]

        while (prefix + k ) //(i - j + 1) < nums[i] and i >= j:
            prefix -= nums[j]
            j += 1

        if ans[0] < i - j + 1:
            ans = [i - j + 1, nums[i]]
    return ans
        
if __name__ == "__main__":

    print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()