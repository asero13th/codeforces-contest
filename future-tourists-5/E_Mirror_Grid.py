import sys
import threading

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
    return list(s[:len(s)])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    nums = []
    ans = 0
    for i in range(n):
        nums.append(insr())
    for i in range(n):
        for j in range(i, n - i - 1):
            a1, b1 = i, j
            a2, b2 = j, n - i - 1
            a3, b3 = n - i - 1, n - j - 1
            a4, b4 = n - j - 1, i

            arr = [nums[a1][b1], nums[a2][b2], nums[a3][b3], nums[a4][b4]]
            c = Counter(arr)

            if len(c) > 1:
                ans += min(c.values())            
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
