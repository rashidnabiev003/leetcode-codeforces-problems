s = "abc"
s = list(s)
l = 0
r = len(s) - 1

def is_pallindrome(left, right):
    while left <= right:
        if s[left] == s[right]:
            right -= 1
            left += 1
        elif s[left] != s[right]:
            return False
    return True

while l <= r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        print(is_pallindrome(l+1, r) or is_pallindrome(l, r-1))
        break

print(True)