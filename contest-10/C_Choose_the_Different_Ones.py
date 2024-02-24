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
    n,m ,k = inlt()
    nums1 = set(inlt())
    nums2 = set(inlt())

    count1, bonus1 = k // 2, 0
    count2 = k//2
    for i in range(1, k + 1):
        if i not in nums1 and i not in nums2:
            return "NO"
        
        if i in nums1 and i in nums2:
            if count1 > 0:
                count1 -= 1
                bonus1 += 1
            else:
                count2 -= 1
                bonus1 -= 1

                if bonus1 < 0 or count2 < 0:
                    return "NO"
        elif i in nums1:
            if not count1 and not bonus1:
                return "NO"
            if not count1:
                bonus1 -= 1
                count2 -= 1

                if bonus1 < 0:
                    return "NO"
            else:
                count1 -= 1
        else:
            if not count2:
                return "NO"
            count2 -= 1
            if count2 < 0:
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
