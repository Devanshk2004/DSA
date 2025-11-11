import math

def find_smallest(arr):
    min = math.inf
    for i in arr:
        if i < min:
            min = i
    return min

arr = list(map(int,input().split()))
print(find_smallest(arr))