# def find_max(arr):
#     if len(arr) == 1:
#         return arr[0]

#     mid = len(arr) // 2
#     left_max = find_max(arr[:mid])
#     right_max = find_max(arr[mid:])

#     return left_max if left_max > right_max else right_max

# def squared_max(arr):
#     if len(arr) == 1:
#         return arr[0] ** 2

#     mid = len(arr) // 2
#     left_squared = squared_max(arr[:mid])
#     right_squared = squared_max(arr[mid:])

#     return left_squared if left_squared > right_squared else right_squared

# def max_pair_sum(arr):
#     if len(arr) == 1:
#         return float('-inf')

#     mid = len(arr) // 2
#     left_part = arr[:mid]
#     right_part = arr[mid:]

#     left_sum = max_pair_sum(left_part)
#     right_sum = max_pair_sum(right_part)

#     max_left = find_max(right_part)
#     max_right = squared_max(left_part)

#     cross_sum = max_left + max_right

#     return max(cross_sum, left_sum, right_sum)

# n = int(input().strip())
# arr = list(map(int, input().split()))

# print(max_pair_sum(arr))

# def linear_max(arr):
#     if len(arr) == 1:
#         return arr[0]

#     mid = len(arr) // 2
#     l = linear_max(arr[:mid])
#     r = linear_max(arr[mid:])

#     if l > r:
#         return l
#     else:
#         return r

# def square_max(arr):
#     if len(arr) == 1:
#         return arr[0] ** 2

#     mid = len(arr) // 2
#     l = square_max(arr[:mid])
#     r = square_max(arr[mid:])

#     if l > r:
#         return l
#     else:
#         return r

# def sum_max(arr):
#     if len(arr) == 1:
#         return None

#     mid = len(arr) // 2
#     l_sum_max = sum_max(arr[:mid])
#     r_sum_max = sum_max(arr[mid:])

#     l_linear_max = linear_max(arr[mid:])
#     r_square_max = square_max(arr[:mid])

#     cross_max_sum = l_linear_max + r_square_max

#     if l_sum_max is None:
#         l_sum_max = float('-inf')
#     if r_sum_max is None:
#         r_sum_max = float('-inf')

#     return max(cross_max_sum, l_sum_max, r_sum_max)

# import io, os
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# n = input()
# arr = list(map(int, input().split()))

# print(sum_max(arr))

def max_pair_value(arr):
    def divide_and_conquer(left, right):
        if left == right:
            return float('-inf')

        mid = (left + right) // 2

        left_max = divide_and_conquer(left, mid)
        right_max = divide_and_conquer(mid + 1, right)

        best_cross = float('-inf')
        max_right = max(arr[mid + 1:right + 1])  # Maximum in the right half

        for i in range(left, mid + 1):
            best_cross = max(best_cross, arr[i] + max_right ** 2)

        return max(left_max, right_max, best_cross)

    return divide_and_conquer(0, len(arr) - 1)

n = int(input())
arr = list(map(int, input().split()))
print(max_pair_value(arr))
