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
    ans = [0,0,0]
    if n <= 6 or n == 9:
        return "NO"
    if n %3 != 0:
        ans[0] = 1
        n -= 1
        ans[1] = 2
        n -= 2
        if n % 3 == 0:
            return "NO"
        else:
            ans[2] = n
            return "YES\n" + " ".join(map(str, ans))
    else:
        n -= 1
        ans[0] = 1
        n -= 4
        ans[1] = 4

        if n % 3 == 0:
            return "NO"
        else:
            ans[2] = n
            return "YES\n" + " ".join(map(str, ans))



if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
