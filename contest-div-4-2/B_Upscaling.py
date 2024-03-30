t = int(input())
for _ in range(t):
    n = int(input())

    start_star = ["##" if i % 2 == 0 else ".." for i in range(n)]
    start_dot = [".." if i % 2 == 0 else "##" for i in range(n)]
    matrix = []
    for i in range(n):
        
        if i % 2 == 0:
            matrix.append(start_star)
            matrix.append(start_star)
        else:
            matrix.append(start_dot)
            matrix.append(start_dot)
    for arr in matrix:
        print("".join(arr))