T = int(input())

for _ in range(T):
    a, n, m = map(int, input().split())

    if a == 1:
        print(n % m)
        continue

    result = 1
    base = a % m
    exp = n + 1 

    while exp > 0:
        if exp % 2 == 1: 
            result = (result * base) % m
        base = (base * base) % m 
        exp //= 2  

    numerator = (result - a + m) % m  
    denominator = pow(a - 1, -1, m)   
    S = (numerator * denominator) % m  

    print(S)
