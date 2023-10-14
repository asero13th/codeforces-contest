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
    px, py = II()
    ax, ay = II()
    bx, by = II()

    def binary(rad):
     
        if ((px - ax)**  2 + (py - ay)  **2 <= rad  ** 2 and (- ax) ** 2 + (- ay) ** 2 <= rad ** 2) or (
               (px - bx)  **2 + (py - by) ** 2 <= rad  **2 and (- bx) ** 2 + (- by)  **2 <= rad ** 2):
            return True
        if  (px - ax)**  2 + (py - ay)  **2 <= rad ** 2 or (px - bx)  **2 + (py - by) ** 2 <= rad ** 2:
            if (- ax) ** 2 + (- ay) ** 2 or (- bx) ** 2 + (- by)  **2:
                if math.sqrt((ax - bx) ** 2 + (by - ay)  ** 2) <= 2 * rad:
                    return True
        return False

    # def binary(mid):
    #     distb = math.sqrt((tx - c2x)  2 + (ty - c2y)  2)
    #     dissb = math.sqrt((c2x)  2 + (c2y)  2)
    #
    #     if dissb <= mid and distb <= mid:
    #         return  True
    #
    #     dista = math.sqrt((tx - c1x)  2 + (ty - c1y)  2)
    #     dissa = math.sqrt((c1x)  2 + (c1y)  2)
    #
    #     if dissa <= mid and dista <= mid:
    #         return True
    #
    #     diameter = math.sqrt((c2x - c1x)  2 + (c2y - c1y)  2)



        # if dissa <= mid or dissb <= mid:
        #     if distb <= mid or dista <= mid:
        #         if 2 * mid <= diameter:
        #             return True



        # return False

    low = 0
    high = 10 ** 6

    while low + (1/( 10 ** 6)) < high:
        mid = (low + high) / 2

        if binary(mid):
            high = mid
        else:
            low = mid

    print( high)

T = I()
for ___ in range(T):
    solve()