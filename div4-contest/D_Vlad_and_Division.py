from collections import  defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    container = defaultdict(int)
    val = 2147483647

    ans = 0
    for num in nums:
        if (val ^ num) in container:
            ans += 1
            container[val ^ num] -= 1
        else:
            container[num] += 1

    for key in container:
        ans += container[key]
    print(ans) 