def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))

def solve():
    x, y, n = inlt()

    ans = []
    for i in range(n - 1 , -1, -1):
        ans.append(x)
        x = x + i
    
    if x > y: return [-1]
    return ans
        

if __name__ == "__main__":

    t = inp()
    for i in  range(t):
        print(*solve())

