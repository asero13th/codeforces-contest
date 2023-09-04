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

    ans = 0

    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            ans += 1
        elif nums[i - 1] > nums[i] < nums[i + 1]:
            ans += 1
    return ans


    


if __name__ == "__main__":

    print(solve())
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
