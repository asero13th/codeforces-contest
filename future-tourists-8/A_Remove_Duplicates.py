from collections import Counter
n = int(input())
nums = list(map(int, input().split()))



def solve(n, nums):
    nums = reversed(nums)
    c =Counter(nums)     
    return [len(c), *reversed(c.keys())]
ans = solve(n, nums)
print(ans[0])
print(*ans[1:])
        
        