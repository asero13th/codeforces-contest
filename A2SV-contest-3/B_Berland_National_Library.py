




def solve():
    n = int(input())
    hashmap = {}
    ans = 0
    for _ in range(n):
        check, name = input().split()
        if check == "+":
            hashmap[name] = 1
        elif check == "-" :
            if name in hashmap:
                del hashmap[name]
            else:
                ans += 1


        ans = max(ans, len(hashmap))
    return ans

print(solve())

