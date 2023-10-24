t = int(input())
for _ in  range(t):
    num = int(input())

    div = num // 2020
    rem = num % 2020

    if num < 2020:
        print("NO")
    elif num % 2020 == 0 or num % 2021 == 0:
        print("YES")
    elif div >= rem:
        print("YES")
    else:
        print("NO")
