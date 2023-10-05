# CodeLight 2023
 
from collections import Counter, defaultdict
 
 
def inp():
    return int(input())
def invr():
    return map(int, input().split())
def invr_list():
    return list(map(int, input().split()))
t = inp()
for _ in range(t):
    n = inp()
    c = defaultdict(int)
    for i in range(n):
        s = input()
        c[s] += 1
 
    d = list(c)
    n = len(d)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if d[i] == d[j]:
                continue
            if d[i][0] == d[j][0] or d[i][1] == d[j][1]:
                ans += c[d[i]] * c[d[j]]
 
    print(ans)