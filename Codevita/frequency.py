def frequency(nums):
    fr = {}
    for i in nums:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    
    for x in fr:
        print(x,fr[x])

nums = list(map(int,input().split()))
frequency(nums)