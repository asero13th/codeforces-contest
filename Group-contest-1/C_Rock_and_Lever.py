import collections
n = int(input())
def getLastBit(n):
    count = 0
    while n > 0:
        n >>= 1
        count += 1
    return count
 
for _ in range(n):
    n = int(input())
    nums = list(map(int,input().split()))
    dic = collections.defaultdict(int)
    count = 0
    for num in nums:
        lastBit = getLastBit(num)
        if lastBit in dic:
            count+= dic[lastBit]
        dic[lastBit] += 1
    print(count)