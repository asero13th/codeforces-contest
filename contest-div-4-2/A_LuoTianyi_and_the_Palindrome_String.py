from collections import Counter

def is_palindrome(s):
    c = Counter(s)
    if len(c) == 1:
        return -1
    if s == s[::-1]:
        return len(s) - 1
    return len(s)
t = int(input())
for _ in range(t):
    s = input()
    print(is_palindrome(s))