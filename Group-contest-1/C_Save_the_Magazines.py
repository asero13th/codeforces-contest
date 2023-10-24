for _ in range(int(input())):
    n=int(input())
    s=input()
    nums=list(map(int,input().split()))
    maxi,li=[0,-2147483647]
    for i in range(n):

        if s[i]=='1':
            maxi += max(nums[i],li)

        if s[i]=='0' or nums[i] < li:
            li = nums[i] 

    print(maxi)