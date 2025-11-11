class Solution:
    def gcd_finder(self, a, b):
        ran = min(a,b)
        max_gcd = 1
        for i in range(1, ran + 1):
            if b % i == 0 and a % i == 0:
                max_gcd = max(max_gcd, i)
        return max_gcd

sol = Solution()
a = int(input())
b = int(input())
print(sol.gcd_finder(a, b))

#class Solution:
#    def gcd_finder(self, a, b):
#        while b != 0:
#            a, b = b, a % b
#        return a
#
#sol = Solution()
#a = int(input())
#b = int(input())
#print(sol.gcd_finder(a, b))