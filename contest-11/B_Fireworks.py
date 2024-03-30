def solve(a, b, c):
    ans = 0
    ans += (c // a) + 1
    # print(ans)
    ans += (c // b) + 1
    return ans

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))