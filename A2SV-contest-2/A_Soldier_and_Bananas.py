k, n, w = list(map(int, input().split()))

ans = [k for i in range(w)]

for i in range(w):
    ans[i] = ans[i] * (i + 1)
print(sum(ans) - n if sum(ans) > n  else 0)