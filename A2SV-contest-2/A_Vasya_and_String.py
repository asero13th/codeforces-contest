
from collections import defaultdict

def inlt():
    return list(map(int, input().split()))

def solve():
    n, k = inlt()
    name = input()
    window = 0
    left = 0
    hashmap = defaultdict(int)
    for i in range(len(name)):
        hashmap[name[i]] += 1

        while len(hashmap) >= 2 and min(hashmap.values()) > k:
            hashmap[name[left]] -= 1
            left += 1

            window = max(window, i - left + 1)
        window = max(window, i - left + 1)
    return window
    
if __name__ == "__main__":

    print(solve())

