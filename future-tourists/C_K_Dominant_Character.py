from collections import defaultdict

#        ---- Input Functions ----      #


def solve():
    s = input()
    ans = len(s) + 1
    for char in set(s):
        string = char + s + char
        curr, prev = 0, 0
        for i in range(1, len(string)):
            if string[i] == char:
                curr = max(curr, i - prev)
                prev = i
        ans = min(ans, curr )
    return ans

if __name__ == "__main__":

    print(solve())
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
