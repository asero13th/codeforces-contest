from collections import Counter, defaultdict
from math import ceil
def solve(n, a):
    right = defaultdict(int)
    for char in a: 
        right[char] += 1

    left = defaultdict(int)
    ans = (n / 2)
    target = 0

    if right['1'] >= right['0']:
        target = 0
    else:
        target = n
  
    for idx, char in enumerate(a):
        # char = a[idx]
        right[char] -= 1
        left[char] += 1

        if left['0'] >= left['1'] and right['1'] >= right['0']:

            if ans > abs((n / 2) - (idx + 1)):
                target = idx + 1
                ans = abs((n / 2) - (idx + 1))
    return target 

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    print(solve(n, a))