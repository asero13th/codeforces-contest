from math import ceil
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    half = ceil(n / 2)
    val = ceil((half + n)/2)
  
    if k <= half:
        print(k * 2 - 1)
    elif k <= val:
      
        print((k - half) * 2) if(k - half) % 2 != 0 else print((k - half + 1) * 2)
    else:
        print((k - val) * 2) if (k - val) % 2 == 0 else print((k - val + 1) * 2 )