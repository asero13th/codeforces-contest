from collections import defaultdict
 
 
 
#        ---- Input Functions ----      #
 
 
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s)])
def invr():
    return map(int, input().split())
def solve():
    n = inp()
    s = input()
    hashmap = {
        'U': 'D',
        'D': 'U',
        'L': 'R',
        'R': 'L'
    }
    count = defaultdict(int)
    for i in s:
        count[i] += 1
    
    side = min(count['L'], count['R'])
    up = min(count['U'], count['D'])

    return max(2 * side + 2 * up, 2 * side + 2 * up)


 
if __name__ == "__main__":
    print(solve())