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
    nums1, nums2 = inlt(), inlt()

    if nums1 == nums2:
        return 0
    before = 0
    for i in range(n):
        if nums1[i] != nums2[i]:
            before += 1

    nums1.sort()
    nums2.sort()

    ans = 1
    for i in range(n):
        if nums1[i] != nums2[i]:
            ans += 1
    return min(ans, before)

if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
