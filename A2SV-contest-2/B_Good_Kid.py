import math
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    nums[0] += 1

    print(math.prod(nums))
