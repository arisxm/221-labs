def max_left(arr):
    if len(arr) == 1:
        return int(arr[0])

    mid = len(arr) // 2
    return max(max_left(arr[:mid:]), max_left(arr[mid::]))

def max_right(arr):
    if len(arr) == 1:
        return int(arr[0]) ** 2

    mid = len(arr) // 2
    return max(max_right(arr[:mid:]), max_right(arr[mid::]))

def max_pair_sum(arr):
    if len(arr) == 1:
        return float('-inf')

    mid = len(arr) // 2
    left_part = arr[:mid:]
    right_part = arr[mid::]

    left_max = max_pair_sum(left_part)
    right_max = max_pair_sum(right_part)
    cross_sum = max_left(left_part) + max_right(right_part)

    return max(left_max, right_max, cross_sum)

n = int(input())
arr = input().split(" ")

print(max_pair_sum(arr))