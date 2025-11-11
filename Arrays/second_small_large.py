import math

def second_s_l(arr):
    if len(arr) < 2:
        print("Array is too small.")
        return None
    
    smallest = math.inf
    s_smallest = math.inf
    largest = -math.inf
    s_largest = -math.inf

    for num in arr:
        if num > largest:
            s_largest = largest
            largest = num
        elif num > s_largest and num != largest:
            s_largest = num
        
        if num < smallest:
            s_smallest = smallest
            smallest = num
        elif num < s_smallest and num != largest:
            s_smallest = num
    
    return (s_smallest,s_largest)

arr = list(map(int,input().split()))
s_small, s_large = second_s_l(arr)
print(f"Second Smallest: {s_small}")
print(f"Second Largest: {s_large}")