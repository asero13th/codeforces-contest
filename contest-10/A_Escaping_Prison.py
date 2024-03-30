t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    rope = 0
    for _ in range(n):
        a, b = map(int, input().split())
        rope += max(b, a)
    if rope >= h:
        print("YES")
    else:
        print("NO")

