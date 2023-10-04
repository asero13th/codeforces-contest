def calculate_points(grid):
    points = 0
    ring_points = [1, 2, 3, 4, 5]
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                distance = min(i, 9 - i, j, 9 - j)
                points += ring_points[distance]
    return points

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the grid
    grid = [input() for _ in range(10)]
    
    # Calculate the points
    points = calculate_points(grid)
    
    # Output the result
    print(points)