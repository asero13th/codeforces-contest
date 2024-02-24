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
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    arr = []
    for i in range(n):
        arr.append(inlt())
    arr.sort(key=lambda x: (x[0], x[1]))
    stack = []
    print(arr)
    for x, y in arr:
        if not stack:
            stack.append((x, y, 1))
        else:
            a, b, flag = stack.pop()
            stack.append(x, y , flag + 1)

            if flag > 2:

    return "YES"





    ans = 0
    print(arr)
        

if __name__ == "__main__":

    print(solve())

