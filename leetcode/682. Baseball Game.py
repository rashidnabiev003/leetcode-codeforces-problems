operations = ["5","-2","4","C","D","9","+","+"]
total_sum = 0
stack = []

for i in operations:
    match i:
        case '+':
            stack.append(stack[-1] + stack[-2])
        case 'C':
            stack.pop()
        case 'D':
            stack.append(stack[-1] * 2)
        case _:
            stack.append(int(i))

print(sum(stack))

