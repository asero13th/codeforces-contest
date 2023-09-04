
def solve():
    n = int(input())
    name = input()
    if sorted(name) == sorted("Timur"):
        return "YES"
    return "NO"




t = int(input())

for _ in range(t):
    print(solve())