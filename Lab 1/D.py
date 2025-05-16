import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
    S = sys.stdin.readline().strip()
    index = S.find("1")

    if index == -1:
        print(index)
    else: print(index+1)
