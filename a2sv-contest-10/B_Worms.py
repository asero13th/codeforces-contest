n = int(input())
piles = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

def solve(n,piles,m,queries):
    prefix_sum = [0]
    for pile in piles:
        prefix_sum.append(prefix_sum[-1] + pile)
    
    for query in queries:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid] < query:
                left = mid + 1
            else:
                right = mid
        print(left)

(solve(n, piles, m, queries))