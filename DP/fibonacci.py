def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

n = int(input())  

dp = [-1] * (n + 1)

result = fib(n, dp)

print(result)


