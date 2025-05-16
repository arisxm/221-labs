import sys
import bisect

n, q = (input().split())
n=int(n)
q=int(q)
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    x, y = input().split()
    x = int(x)
    y = int(y)
    left_index = bisect.bisect_left(arr, x)  
    right_index = bisect.bisect_right(arr, y) 
    print(right_index - left_index)







