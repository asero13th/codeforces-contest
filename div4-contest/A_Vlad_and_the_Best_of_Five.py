from collections import Counter
n = int(input())
for _ in range(n):
    string  = input()
    c = Counter(string)
    if c['A'] > c['B']:
        print('A')
    else:
        print('B')