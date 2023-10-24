string = input()
stack = []

hello = ['h', 'e', 'l', 'l', 'o']
i = 0
for char in string:
    if char == hello[i]:
        i += 1
    if i >= len(hello) :
        print("YES")
        break
else:
    print('NO')

    
