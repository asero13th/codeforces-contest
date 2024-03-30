n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduce(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    return num

def is_possible(nums):
    nums = [reduce(num) for num in nums]
    return len(set(nums)) == 1

print("Yes" if is_possible(nums) else "No")