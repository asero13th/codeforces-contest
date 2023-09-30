
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[0] * 3 for _ in range(n)]
    
    dp[0][0] = 0
    dp[0][1] = a[0]
    dp[0][2] = b[0]


    for i in range(1, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + a[i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + b[i]

    return max(dp[-1])
print(solve())