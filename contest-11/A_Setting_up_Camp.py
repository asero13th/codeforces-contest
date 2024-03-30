def solve(a, b, c):
    ans = a
    bs = (b // 3)
    brem = (b % 3)
    if brem != 0 and c < (3 - brem):
        return -1

    ans += bs
    if brem != 0:
        c -= (3 - brem)
    if brem != 0:
        ans += 1
    
    if c > 0:
        ans += (c // 3)
        if c % 3 != 0:
            ans += 1
    
    return ans





t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))