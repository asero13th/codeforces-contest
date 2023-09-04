from collections import defaultdict
import sys, threading
def main():
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        color = input()
        tree = defaultdict(list)
 
        for i in range(n-1):
            tree[arr[i]].append(i+2)
        
        count = 0
        def dfs(node):
            nonlocal count
            white = 1 if color[node-1] == 'W' else 0
            black =  1 if color[node-1] == 'B' else 0
            for child in tree[node]:
                w, b = dfs(child)
                white += w
                black += b
            
            if white == black:
                count += 1
            
            return white, black
 
        dfs(1)
 
        print(count)
 
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()