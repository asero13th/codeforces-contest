


#        ---- Input Functions ----      #


def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    a = inlt()

    
    stack = [0] * n

    for i in range(n - 1,0, -2):
        first, second = a[i], a[i - 1]
        if first < second:
            first, second = second, first
        stack[i] = first
        stack[i - 1] = second

    if len(a) % 2 != 0:
        stack[0] = a[0]
    
    a.sort()
    for i, num in enumerate(a):
        if num != stack[i]:
            return "NO"
    return "YES"

if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
