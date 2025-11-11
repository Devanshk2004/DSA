def inde(nums):
    half = len(nums)//2
    nums[:half] = sorted(nums[:half])
    nums[half:] = sorted(nums[half:],reverse = True)
    return nums

nums = list(map(int,input().split()))
print(*inde(nums))