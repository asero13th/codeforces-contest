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
    memo = defaultdict(list)
    for _ in range(n):
        post = input().split()
        person1, person2 = post[0], post[2]
        p1, p2 = [],[]
        for char in person1:
            if char.isupper():
                p1.append(char.lower())
            else:
                p1.append(char)
        for char in person2:
            if char.isupper():
                p2.append(char.lower())
            else:
                p2.append(char)
        p1 = "".join(p1)
        p2 = "".join(p2)
        memo[p2].append(p1)
    
    #
    keys = list(memo.keys())
    
    def max_depth(graph, start):
        max_depth = 0
        stack = [(start, 0)]

        while stack:
            node, depth = stack.pop()

           
            if depth > max_depth:
                max_depth = depth

            for neighbor in graph[node]:
                stack.append((neighbor, depth + 1))

        return max_depth

    answer = 0 
    for key in keys:
        answer = max(answer, max_depth(memo, key))
    return answer + 1
                



        

if __name__ == "__main__":
    print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
