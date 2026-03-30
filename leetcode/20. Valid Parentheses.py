s = "()"
stack = []
stack_len = 0

for i in s:
    if i == "(" or i == "[" or i == "{":
        stack.append(i) 
        stack_len += 1
    else:
        if stack_len == 0:
            print(False)
            break
        if i == "]" and stack.pop() != "[":
            print(False)
        elif i == ")" and stack.pop() != "(":
            print(False)
        elif i == "}" and stack.pop() != "{":
            print(False)
        stack_len -= 1

print(True if len(stack) == 0 else False)
         
