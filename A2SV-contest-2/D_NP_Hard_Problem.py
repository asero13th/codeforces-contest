import sys
import math
import bisect
import heapq
import itertools
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right

mod=1000000007

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))


def solve():
    n = int(input())
    nums = get_list()
    root = [None, None]
    def insert(word):
        curr = root
        for char in word:
            if not curr[int(char)]:
                curr[int(char)] = [None, None]
            curr = curr[int(char)]
    
    def maxXOR(num1, num2, answer):
        nonlocal answers
        found = False

        if len(answer) == 32:
            answers.append(int(answer, 2))
            return

        for i in range(2):
            if num1[i] and num2[1-i]:
                found = True
                maxXOR(num1[i], num2[1-i], answer+"1")
        
        if not found:
            for i in range(2):
                if num1[i]:
                    maxXOR(num1[i], num2[i], answer+"0")
    

    if len(nums) == 1:
        return 0
    
    for num in nums:
        insert(format(num, '032b'))
    answers = []
    
    maxXOR(root, root, "")
    return max(answers)



               
if __name__ == "main":
    for _ in range(int(input())):
        print(solve())