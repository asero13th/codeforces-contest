import math
import sys


def I(): return int(input())


def II(): return map(int, sys.stdin.readline().rstrip().split())


def IL(): return list(map(int, input().split()))


def SIL(): return sorted(map(int, input().split()))


def RSIL(): return sorted(map(int, input().split()), reverse=True)


from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, _heapify_max, nlargest, nsmallest
import copy


# sys.setrecursionlimit(2500)


def solve():
    n, m = II()
    a = input()
    b = input()

    leng = len(b)
    lsp = [0] * leng

    prevLsp, i = 0, 1

    while i < leng:
        if b[i] == b[prevLsp]:
            prevLsp += 1
            lsp[i] = prevLsp
            i += 1

        elif prevLsp == 0:
            lsp[i] = 0
            i += 1
        else:
            prevLsp = lsp[prevLsp - 1]

    i, j = 0, 0
    factors = 1
    count = 0
    answer = 0
    found = 0

    while i <= len(a):
        if i == len(a):
            count += 1
            # print(count, factors, answer)
            if count == factors:
                answer += 1
                factors += factors
            i = 0
        if a[i] == b[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
            if answer > 1:
                break
        else:

            j = lsp[j - 1]
            if answer > 1:
                break

        if j == leng:
            print(answer)
            found = 1
            break

    if not found:
        print(-1)


T = I()
for ___ in range(T):
    solve()
  