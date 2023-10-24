import math
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, _heapify_max, nlargest, nsmallest

sys.setrecursionlimit(2500)


def solve():
    s = input()
    length = len(s)
    totOne = s.count('1')
    totZero = s.count('0')

    doneZero = 0
    doneOne = 0
    minMov = min(totOne, totZero)

    for index in range(length):
        if s[index] == '1':
            doneOne += 1

        else:
            doneZero += 1
        
        movOne = doneZero + (totOne - doneOne)
        movZero = doneOne + (totZero - doneZero)
        minMov = min(movZero, movOne,  minMov)

    print(minMov)

T = I()
for ___ in range(T):
    solve()