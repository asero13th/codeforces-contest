n = int(input())
nums = input()

def solve(nums):
    

    j = 0
    ans = 0
    for i in range(len(nums)):
        if nums[i] == "x" and (i - j + 1) > 2:
            ans += 1
        
        elif nums[i] != "x":
            j = i + 1
        
    return ans
print(solve(nums))

        
    