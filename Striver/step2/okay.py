class Solution:
    def divisor(self, n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors


sol = Solution()
n = int(input())
print(sol.divisor(n))