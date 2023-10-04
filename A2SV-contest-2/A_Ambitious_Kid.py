n = int(input())
nums = list(map(int, input().split()))

for idx, num in enumerate(nums):
    nums[idx] = abs(num)

print(min(nums))