class Solution:
    def armstrong(self, n):
        str_n = str(n)
        n_len = len(str_n)
        sum_of_powers = sum(int(digit) ** n_len for digit in str_n)
        return sum_of_powers == n

sol = Solution()
n = int(input())
print(sol.armstrong(n))