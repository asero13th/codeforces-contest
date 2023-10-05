import heapq


#write a function that calculate the number of productive meeting
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    #create a heap
    
    heap = []
    for i in range(n):
        if nums[i] > 0:
            heapq.heappush(heap, ( -1 * nums[i], i + 1))
    ans = []
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        a = (a[0] + 1, a[1])
        b = (b[0] + 1, b[1])

        if -1 * a[0] > 0:
            heapq.heappush(heap, a)
        if -1 * b[0] > 0:
            heapq.heappush(heap, b)
        ans.append((a[1], b[1]))
    print(len(ans))
    for i in ans:
        print(i[0], i[1])

t= int(input())
for _ in range(t):
    solve()