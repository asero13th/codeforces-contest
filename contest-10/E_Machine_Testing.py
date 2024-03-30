def solve(n, health, power):
    
    

t  = int(input())
for _ in range(t):
    n = int(input())
    helth = list(map(int, input().split()))
    power = list(map(int, input().split()))

    print(solve(n, helth, power))
