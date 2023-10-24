from collections import defaultdict

entrance = defaultdict(int) 
exit = defaultdict(int)
 
n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))


for idx, num in enumerate(nums1):
    entrance[num] = idx 

i = 0
visited = set()
ans = 0
for idx, val in enumerate(nums2):
    if i < len(nums1) and nums1[i] in visited:
            i += 1    
    if val not in visited and val != nums1[i] :
        ans += 1
        
    elif val == nums1[i]:
        i += 1
    
    visited.add(val)
print(ans)

