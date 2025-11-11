def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not")

s = input()
palindrome(s)