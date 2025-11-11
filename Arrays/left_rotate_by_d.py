#def left_rotate(arr, n, d):
#    d = d % n  
#    temp = arr[:d] 
#
#    for i in range(d, n):
#        arr[i - d] = arr[i]
#
#    for i in range(n - d, n):
#        arr[i] = temp[i - (n - d)]

def left_rotate_ez(arr,d):
    d = d % n
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    arr[:] = reversed(arr)

n = int(input())
arr = list(map(int, input().split()))
d = int(input())

left_rotate_ez(arr, d)

print("Rotated array:")
print(*arr)

#yup