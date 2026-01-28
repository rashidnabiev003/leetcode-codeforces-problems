haystack = "sadbutsad"
needle = "sad"
haystack = list(haystack)
needle =list(needle)

l = 0
r = 0

while l <= len(haystack) - r - 1:
    if haystack[l + r] == needle[r]:
        r += 1
        if r == len(needle):
            print(l)
            break
    else:
        l += 1
        r = 0


        