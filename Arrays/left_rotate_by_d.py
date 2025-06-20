def left_rotate(arr, n, d):
    d = d % n  # Handle cases where d > n
    temp = arr[:d]  # Store first d elements

    # Shift the rest of the array to the left
    for i in range(d, n):
        arr[i - d] = arr[i]

    # Copy the temp elements to the end
    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]


# Main logic
n = int(input())
arr = list(map(int, input().split()))
d = int(input())

left_rotate(arr, n, d)

# Output the result
print("Rotated array:")
print(*arr)
