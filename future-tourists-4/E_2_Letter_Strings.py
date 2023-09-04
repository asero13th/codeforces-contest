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
    return list(s[:len(s)])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    strings = []
    word = defaultdict(list)
    count = defaultdict(int)
    for _ in range(n):
        tmp = input()
        letter1, letter2 = tmp[0], tmp[1]
        if letter2 != letter1:
            word[letter1].append(letter2)
            word[letter2].append(letter1)
        count[letter1] +=  1
        count[letter2] += 1

    
    print(word)
    ans = 0
    count = Counter(strings)
    for key, val in count.items():
        letter1, letter2 = key[0], key[1]
        if letter1 != letter2:
            ans += max(word[letter1], word[letter2])
    return ans


if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
