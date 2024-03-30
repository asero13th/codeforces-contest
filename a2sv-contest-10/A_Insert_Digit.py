def solve(n, m, nums):
    nums = list(nums)
    
    for idx, num in enumerate(nums):
        if int(num) < m:
            nums.insert(idx, str(m))
            return ''.join(nums)
    nums.append(str(m))
    return ''.join(nums)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    num = input()

    print(solve(n, m, num))

