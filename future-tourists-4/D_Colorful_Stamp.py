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
    color = input()
    
    red, blue = 0, 0
   
    for i, c in enumerate(color):

        if c == "R":
            red += 1

        if c == "B":
            blue += 1

        if c == "W" or i == len(color) - 1:
     
            if red == 0 and blue == 0:
                red = 0
                blue = 0
            elif red == 0 or blue == 0:
                return "NO"
            
            red = 0
            blue = 0

    return "YES"
            
            
        

        
        
        

    


if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
