
t = int(input())

for _ in range(t):

    n = int(input())
    nums = list(map(int, input().split()))
    
    hashmap = {}
    answer = 0

    for idx, num in enumerate(nums):
        if num - (idx + 1) in hashmap:
            answer += hashmap[num - (idx + 1)]
            hashmap[num - (idx + 1)] += 1
        else:
            hashmap[num - (idx + 1)] = 1

    print(answer)