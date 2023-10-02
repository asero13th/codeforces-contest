n, m = map(int, input().split())
dorms = list(map(int, input().split()))
letters = list(map(int, input().split()))
from itertools import accumulate

def solve(dorms, letters):
    runningSum = list(accumulate(dorms))
    ans = []

    for letter in letters:
        index, value = binarSearch(letter, runningSum)
        ans.append((index + 1, abs(dorms[index] - (value - letter))))
    
    return ans
    

def binarSearch(target, arr):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2

        if arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return i, arr[i]

ans = (solve(dorms, letters))
for i in ans:
    print(i[0], i[1])