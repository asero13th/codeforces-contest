

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    j = 0
    ans = 0
    for idx, num in enumerate(nums):
        if num == 1:
            j = idx + 1
            
        ans = max(ans, idx - j + 1)
    return ans
        

        



t = int(input())
for _ in range(t):
    print(solve())