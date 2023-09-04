def solve():
    color = {
        "R": "R",   
        "G": "B",
        "B": "G",
    }
    n = int(input())
    a, b = input(), input()

    for i in range(n):
        if a[i] == b[i]:
            continue
        elif color[a[i]] != b[i]:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    print(solve())