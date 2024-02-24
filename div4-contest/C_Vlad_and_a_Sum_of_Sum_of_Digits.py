prefix = [0]
for i in range(1, 2 * 100000 + 1):
    prefix.append(prefix[-1] + sum(map(int, str(i))))
# print(prefix)
t = int(input())
for _ in range(t):
    r = int(input())
    # print(r)
    print(prefix[r])