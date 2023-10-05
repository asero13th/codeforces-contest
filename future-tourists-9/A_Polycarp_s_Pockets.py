from collections import Counter
n = int(input())
nums = list(map(int, input().split()))

print(max(Counter(nums).values()))
