

def solve():
    n, k = list(map(int, input().split()))
    a = input()

    arr = []
    for i, char in enumerate(a):
        if char == "B":
            arr.append(i)
    ans = 0
    j = 0

    for i in range(1, len(arr)):
        if (arr[i] - arr[j] + 1) > k:
            ans += 1
            j = i 
    
        
    return ans + 1 if arr else 0


t = int(input())
for _ in range(t):
    print(solve())
