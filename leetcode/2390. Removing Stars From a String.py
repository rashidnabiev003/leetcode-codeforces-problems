s = "leet**cod*e"

stack = []

for char in s:
    if char == '*':
        if stack:
            stack.pop()
    else:
        stack.append(char)

print(''.join(stack))