a, b = map(int, input().split())

MOD = 107
result = 1
base = a % MOD 

while b > 0:
    if b % 2 == 1: 
        result = (result * base) % MOD
    base = (base * base) % MOD
    b //= 2 

print(result)