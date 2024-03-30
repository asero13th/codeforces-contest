from collections import Counter
from fractions import Fraction

n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

bonus = 0
for i in range(n):
    if nums1[i] == 0 and nums2[i] == 0:
        bonus += 1

divisor = [Fraction(-nums2[i] ,nums1[i]) for i in range(n) if nums1[i] != 0]
maximum = 0

c = Counter(divisor)
for key in c:
    maximum = max(maximum, c[key])

print(maximum + bonus)