import itertools

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()

    num1 = [ord(char) for char in w]
    num2 = [ord(char) for char in s]

    sum1 = sum(num1)
    prefix = 0
    hashmap = {0:-1}
    for i in range(n):
        prefix += num2[i]
        
        if prefix - sum1 in hashmap and i - hashmap[prefix - sum1] == m:
            print("YES")
            break
        
        hashmap[prefix] = i
    else:
        print("NO")