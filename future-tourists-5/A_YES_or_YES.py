


#        ---- Input Functions ----      #



def solve():
    string = input()

    if "".join((string.upper())) == "".join(("YES")):
        return "YES"
 
    else:
        return "NO"

if __name__ == "__main__":

    t = int(input())
    for i in range(t):
        print(solve())

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=solve)
# main_thread.start()
# main_thread.join()
