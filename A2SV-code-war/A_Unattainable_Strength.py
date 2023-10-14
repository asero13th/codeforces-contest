import sys
import threading

input = sys.stdin.readline
from collections import Counter
import itertools
from math import ceil, floor, log
from collections import defaultdict
from collections import deque
from itertools import accumulate


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
    n= inlt()
    artifacts = inlt()

    artifacts.sort()
    current_sum = 0

    for artifact in artifacts:
        if artifact > current_sum + 1:
           
            return current_sum + 1
        current_sum += artifact

    return current_sum + 1
        

    


if __name__ == "__main__":

    print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
