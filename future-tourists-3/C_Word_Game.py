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
    a, b, c = input().split(), input().split(), input().split()
    hasha, hashb,hashc = Counter(a), Counter(b), Counter(c)
    a = set(a)
    b = set(b)
    c = set(c)
    ansa, ansb, ansc = 0,0,0
   
    for val in a:
        if val not in b and val not in c:
            ansa += 3
        elif val  in b and val  in c:
            ansa += 0
        elif val in b or val in c:
            ansa += 1
    for val in b:
        if val not in a and val not in c:
            ansb += 3
        elif val  in a and val  in c:
            ansb += 0
        elif val in a or val in c:
            ansb += 1
    for val in c:
        if val not in b and val not in a:
            ansc += 3
        elif val  in b and val  in a:
            ansc += 0
        elif val in b or val in a:
            ansc += 1
    return ansa, ansb, ansc


            
if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
