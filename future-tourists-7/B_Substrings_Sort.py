n = int(input())
words = []
for _ in range(n):
    words.append(input())
words.sort(key=len)
for i in range(n-1):
    if words[i+1].find(words[i]) == -1:
        print("NO")
        break
else:
    print("YES")
    for i in words:
        print(i)