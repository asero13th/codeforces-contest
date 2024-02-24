
t = int(input())
for _ in range(t):
    n = int(input())
    grid = {}
    length = 0
    for _ in range(n):
        tmp = input()
        grid[_] = tmp.count("1")
        length = max(length, grid[_])
    # print(grid)
    for col in grid:
        if grid[col] != length and grid[col] != 0:
            print("TRIANGLE")
            break
    else:
        print("SQUARE")



    