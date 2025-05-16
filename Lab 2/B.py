import sys
#data = sys.stdin.readline().split()
N = int(sys.stdin.readline().strip())
arrN = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline().strip())
arrM = [int(x) for x in sys.stdin.readline().split()]

x, y = 0,0
merged = []

while x<N and y<M:
    if arrN[x]<arrM[y]:
        merged.append(arrN[x])
        x+=1

    elif arrN[x]>arrM[y]:
        merged.append(arrM[y])
        y+=1


if x<N:
    merged.extend(arrN[x:])
    
elif y<M:
    merged.extend(arrM[y:])
    
# sys.stdout.write(" ".join(str(num) for num in merged) + "\n")
print(*merged)