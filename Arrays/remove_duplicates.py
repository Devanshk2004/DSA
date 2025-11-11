def removeDuplicates(nums):
    if not nums:
        return []

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return nums[:i+1]

# Input
nums = list(map(int, input().split()))

# Process and output
result = removeDuplicates(nums)
print(*result)
