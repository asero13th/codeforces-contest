


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    if n == 1:
        return "YES"
    
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 1:
            return "NO"
    return "YES"






t = int(input())
for _ in range(t):
    print(solve())