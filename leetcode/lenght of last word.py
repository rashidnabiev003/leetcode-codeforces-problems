#s = "Hello World"
s = "luffy is still joyboy     "
length = len(s) - 1
iter = 0

while length >= 0:
    if s[length].isalnum():
        iter += 1
        length -= 1
    else:
        if iter == 0:
            length -= 1
        else:
            break

print(iter)