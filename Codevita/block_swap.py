def niger(n,nums):
    s_h = nums[n:]
    for i in range(n):
        s_h.append(nums[i])
    return s_h

n = int(input())
nums = list(map(int,input().split()))
print(*niger(n,nums))

