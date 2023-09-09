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
    letter = input()
    dictionary = {
        "a" : 1, "b" : 2,"c" : 3,"d" : 4,"e" : 5,"f" : 6,"g" : 7,"h" : 8,"i" : 9,"j" : 10,"k" : 11,"l" : 12,"m" : 13,"n" : 14,"o" : 15,"p" : 16,"q" : 17,
        "r" : 18,"s" : 19,"t" : 20,"u" : 21,"v" : 22,"w" : 23,"x" : 24,"y" : 25,"z" : 26
    }
    first, second = letter[0], letter[1]
    val = ((dictionary[first]  - 1) * 25) + dictionary[second]

    if first < second:
        val  -= 1
    return val
    
    
if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
