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
    n, p = inlt()
    arr = inlt()
    

   
    prefix = 0
    summ = sum(arr)
    index = 0
    
    arr = arr + arr
    length = len(arr)

    if summ > p:
        count = p // summ
        length = count + 1
        


    prefix, left = 0, 0
    for right, num in enumerate(arr):

        prefix += num

        while prefix > p:
            
            if right - left + 1 < length:
                index = left
                length = right - left + 1

            prefix -= arr[left]
            left += 1

    return index + 1, length

if __name__ == "__main__":
    print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
