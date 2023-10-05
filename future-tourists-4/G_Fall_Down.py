from collections import *
from functools import reduce
from itertools import *
from heapq import *
from sys import *
from threading import *
 
dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dirs8 = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1,1]]
 
def _input(): return stdin.readline().rstrip("\r\n") 
def I(): return int(_input())
def II(): return _input()
def III(): return map(int, _input().split())
def IV(): return list(map(int, _input().split()))
def V(): return sorted(list(map(int, _input().split())))
def out(var): stdout.write(str(var) + "\n") 
def Solve():
    R, C = III()
    grid = []
    for _ in range(R):
        grid.append(list(II()))
    for i in range(C):
        j = R - 1
        pos = R - 1
        while j > -1:
            if grid[j][i] == '.':
                pass
            elif grid[j][i] == 'o':
                pos = j - 1
            else:
                if pos > j:
                    grid[pos][i], grid[j][i] = grid[j][i], grid[pos][i]
                    pos -= 1
                elif pos == j:
                    pos = j - 1
            j -= 1
    for i in range(R):
        print("".join(grid[i]))
    print("")
T = I()
for ___ in range(T):
    Solve()