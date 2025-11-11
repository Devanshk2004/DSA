def is_palindrome(n):
    str_int = str(n)
    if str_int == "".join(reversed(str_int)):
        print("True")
    else:
        print("False")

n = int(input())
is_palindrome(n)