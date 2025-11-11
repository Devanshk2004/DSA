def move_zeroes(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i]!=0:
            temp.append(nums[i])
    
    for i in range(len(temp)):
        nums[i] = temp[i]
        non_zero = len(temp)

    for i in range(non_zero,len(nums)):
            nums[i] = 0
    
    return nums

nums = list(map(int,input().split()))
result = move_zeroes(nums)
print(result)

