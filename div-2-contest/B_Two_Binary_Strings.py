#backtrack
import sys

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
    a, b = insr(), insr()
    for i in range(len(a) - 1):
        if a[i] == b[i] == a[0]  and a[i + 1] == b[i + 1] == a[-1]:
            return "YES"
    return "NO"



if __name__ == "__main__":
    t = inp()
    for _ in range(t):
        print(solve())