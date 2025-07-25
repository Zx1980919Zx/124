def is_palindrome(s):
    return s == s[::-1]
s = input("топот").strip("топот")
if is_palindrome(s):
    print("yes")
else:
    print("no")