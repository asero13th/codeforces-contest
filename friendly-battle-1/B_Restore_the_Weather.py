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
    a, b = inlt(), inlt()

    sorted_indexes = sorted(list(range(len(a))), key=lambda i: a[i])

    ans = [0] * n
    b.sort()
    for i in range(len(b)):
        ans[sorted_indexes[i]] = b[i]
    return ans


if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
