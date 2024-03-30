def checkTime(n, k, water, time, middle):
    total_time = 0
    for i in range(n):
        trips_needed = max(1, (water[i] + middle - 1) // middle)  
        total_time += trips_needed * time[i]  
        if total_time > k:
            return False  
    return True

def solve(n, k, water, time):
    i, j = 1, max(water)  
    while i <= j:
        middle = (i + j) // 2
        if checkTime(n, k, water, time, middle):
            j = middle - 1  
        else:
            i = middle + 1 
    return i if i <= max(water) else -1  

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    water = list(map(int, input().split()))
    time = list(map(int, input().split()))
    if sum(time) > k:
        print(-1)  
        continue
    print(solve(n, k, water, time))

