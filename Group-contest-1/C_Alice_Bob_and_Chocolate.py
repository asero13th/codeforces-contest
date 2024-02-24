from collections import deque

class Eater:
    def __init__(self):
        self.ate = 0
        self.wait = 0

alice = Eater()
bob = Eater()

n = int(input())
chocs = deque()
nums = list(map(int, input().split()))
for num in nums:
    chocs.append(num)
while len(chocs) > 0:
    if alice.wait != 0:
        alice.wait -= 1
    if bob.wait != 0:
        bob.wait -= 1
    if alice.wait == 0:
        alice.wait = chocs[0]
        alice.ate += 1
        chocs.popleft()
    if bob.wait == 0:
        if len(chocs) == 0:
            break
        else:
            bob.wait = chocs[-1]
            bob.ate += 1
            chocs.pop()

print(alice.ate, bob.ate)