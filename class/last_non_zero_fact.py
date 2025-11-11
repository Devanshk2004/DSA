def factorial(num): 
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result    

def non_zero(fact):
    while fact % 10 == 0:
        fact //= 10
    return fact % 10    

num = int(input())

fact = factorial(num)
print("Factorial is:", fact)

last_digit = non_zero(fact)
print("Last non-zero digit is:", last_digit)
