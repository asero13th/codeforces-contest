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
    words = []
    for i in range(n):
        words.append(input())
    ans = []
    words_set = set(words)
    for val in words:
        for i in range(len(val)):
            if val[:i] in words_set and val[i:] in words_set:
                ans.append("1")
                break
        else:
            ans.append("0")
    return "".join(ans)



if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
