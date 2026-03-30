s = "Pp"
stack = []
for i in s:
    if stack and i.islower() and stack[-1] == i.upper():
        stack.pop()
        continue
    if stack and i.isupper() and stack[-1] == i.lower():
        stack.pop()
        continue
    stack.append(i)

print(''.join(stack))