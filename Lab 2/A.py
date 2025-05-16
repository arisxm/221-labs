N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, N-1
found = False
while left<right:
    if arr[left] + arr[right] == S:
        found = True
        print(left+1, right+1)
        break
        

    elif (arr[left]+arr[right]) < S:
        left +=1

    elif (arr[left]+arr[right]) > S:
        right -=1
    
if found == False:
    print("-1")            


