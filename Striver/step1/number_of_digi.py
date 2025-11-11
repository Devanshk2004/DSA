class Solution:
    def countDigit(self, n):
        count = 0
        while n != 0:
            n = n//10
            count = count + 1
        
        return count

sol = Solution()
n = int(input())
print(sol.countDigit(n))
