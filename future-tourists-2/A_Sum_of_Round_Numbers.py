import sys

def solve():
    nums = input()
    ans = []
    n = len(nums)
    ans = []
    
    
    
    for i, val in enumerate(nums):
        if val.isdigit() and val != "0":
            bet = n - i - 1
            newval = int(val) * (10 ** bet)
            ans.append(newval)
    print(len(ans))
    return ans
    
if __name__ == "__main__":

    t = int(input())
    for i in range(t):
        print(*solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
