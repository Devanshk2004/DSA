def reversed(n):
    left = 0
    right = len(n) - 1
    while left < right:
        n[left],n[right] = n[right],n[left]
        left += 1
        right -= 1 
    return n

n = list(map(int,input().split()))
print(*reversed(n))