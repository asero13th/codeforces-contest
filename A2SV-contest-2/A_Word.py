string = input()
u, l = 0, 0
for char in string:
    if char.isupper():
        u += 1
    else:
        l += 1
print(string.upper() if u > l else string.lower())
