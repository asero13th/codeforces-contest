

t = int(input())


for _ in range(t):
    n = int(input())
    a = input()
    ans = 0
    for i in range(1, n-1):
        if a[i - 1] == a[i + 1]:
            continue
        ans += 1
    print(ans + 1)
