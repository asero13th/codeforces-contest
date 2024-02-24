
from collections import defaultdict
def solve():
    string = input()
    another = string[::-1]
    hashmap = defaultdict(int)
    
    for char in "abcdefghijklmnopqrstuvwxyz":
        idx = another.find(char)
        if idx != -1:
            hashmap[char] = idx
    minimum = min(hashmap.keys())
    index = hashmap[minimum]
    stack = []
    ans = []
    for idx, char in enumerate(string):
        if char == minimum:
            ans.append(char)
            continue
            
        elif index < idx:
            if hashmap:
               
                hashmap.pop(char)
            while hashmap and  hashmap[min(hashmap.keys())] < index:
                hashmap.pop(min(hashmap.keys()))
            if hashmap:
                minimum = min(hashmap.keys())
                index = hashmap[minimum]

        if char != minimum:
            stack.append(char)

    return "".join(ans) + "".join(reversed(stack))

if __name__ == "__main__":
    print(solve())

