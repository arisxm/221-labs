n = int(input())
arr = list(map(int, input().split()))

temp_arr = arr.copy()
inv_count = 0

size = 1
while size < n:
    left = 0
    while left < n - 1:
        mid = min(left + size - 1, n - 1)
        right = min(left + 2 * size - 1, n - 1)

        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1) 
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        left += 2 * size

    size *= 2 

print(inv_count)
print(*arr)