n, k = map(int, input().split())
nums = list(map(int, input().split()))

tmp = list(set(nums))
if len(tmp) >= k:
    print("YES")
    for i in range(k):
        print(nums.index(tmp[i])+1, end=" ")
else:
    print("NO")