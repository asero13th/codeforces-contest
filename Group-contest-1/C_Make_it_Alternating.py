MOD = 998244353

def upd(a, b):
    return (a * b) % MOD

t = int(input())
for _ in range(t):
    s = input()
    res = 1
    k = len(s)
    n = len(s)
    l = 0
    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:
            r += 1
            
        res = upd(res, r - l)
        k -= 1
        l = r

    for i in range(1, k + 1):
        res = upd(res, i)
    print(k, res)