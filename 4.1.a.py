def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True
s = input("топот").strip("топот")
if is_palindrome(s):
    print("yes")
else:
    print("no")