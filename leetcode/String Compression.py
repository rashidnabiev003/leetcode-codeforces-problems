chars = ["a","a","b","b","c","c","c"]

from collections import Counter
array = Counter(chars)

read = 0
write = 0

while read < len(chars):
    char = chars[read]
    l = read
    flag = True
    count = 0
    while l < len(chars) and flag:
        if char == chars[l]:
            count += 1
        else:
            flag = False
        l += 1

    chars[write] = char
    write += 1
    if count > 1:
        for s in str(count):
            chars[write] = s
            write += 1
    read  += count

print(write)




