s = "(()())(())"
stack = []
primitivs_array = []
ans = []

for i in range(len(s)):
    if s[i] == "(":
        if len(stack) == 0:
            primitivs_array.append(i)
        stack.append(s[i])
        continue
    if s[i] == ")" and stack[-1] == "(":
        stack.pop()
        if len(stack) == 0:
            primitivs_array.append(i)

for i in range(len(s)):
    if i not in primitivs_array:
        ans.append(s[i])

print(''.join(ans))


#Более оптимальный вариант
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0  # Счётчик вместо стека
        
        for char in s:
            if char == '(':
                if depth > 0:  # Не внешняя скобка
                    result.append(char)
                depth += 1
            else:  # char == ')'
                depth -= 1
                if depth > 0:  # Не внешняя скобка
                    result.append(char)
        
        return ''.join(result)   

    
