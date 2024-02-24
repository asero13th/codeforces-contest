from collections import Counter
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def solve():
    n = inp()
    name = inlt()

    lowercase_letters = []
    for ascii_value in range(97, 123):  # ASCII values for 'a' to 'z'
        lowercase_letters.append(chr(ascii_value))
    c = Counter(name)
    ans = []
    original = Counter(name)
    for val in name:
        if c[val] >= 0:
            ordval = original[val] -  c[val]
            char = lowercase_letters[ordval]
            c[val] -= 1
            ans.append(char)
    return ''.join(ans)

if __name__ == "__main__":

    t = inp()
    for i in range(t):
        print(solve())
