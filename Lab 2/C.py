import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
current_sum = 0
max_length = 0

for right in range(N):
    current_sum += arr[right]

    if current_sum > K:
        current_sum -= arr[left]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)