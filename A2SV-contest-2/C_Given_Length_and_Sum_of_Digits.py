#given positive integer m and non negetive integer s find the smallest and largest number with length m and sum of digits s
def getMin(arr):
    ans = list(map(int, arr))
    return min(ans)

def smallest(m,s):
    ans = [0 for i in range(m)]
    s -= 1

    for i in range(m - 1, 0, -1):
        if s > 9:
            ans[i] = 9
            s -= 9
        else:
            ans[i] = s
            s = 0
    ans[0] = s + 1
    ans = list(map(str, ans))
   
    return int("".join(map(str, ans))) 


def largest(m,s):
    ans = [0 for i in range(m)]
    for i in range(m):
        if s > 9:
            ans[i] = 9
            s -= 9
        else:
            ans[i] = s
            s = 0
    return int("".join(map(str, ans)))



if __name__ == "__main__":
    m,s = map(int, input().split())
    
    if m == 1 and s == 0:
        print(0,0)
    elif s == 0:
        print(-1,-1)

    elif (s) > m * 9:
        print(-1,-1)
    else:
        ans = [smallest(m,s), largest(m,s)]
        print(*ans)