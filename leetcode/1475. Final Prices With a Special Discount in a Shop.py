prices = [8,4,6,2,3]
stack = []
answer = prices[:]

for i in range(len(prices)):
    while stack and prices[i] <= prices[stack[-1]]:
        prev_indx = stack.pop()
        answer[prev_indx] = prices[prev_indx] - prices[i]
    stack.append(i)

print(answer)