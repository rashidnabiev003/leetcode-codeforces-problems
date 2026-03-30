n = int(input())

def solve(array_len, array):
    stack = []
    answer = 0
    for i in range(array_len):
        if stack and array[i] < stack[-1]:
            answer +=1
            stack.pop()
        stack.append(array[i])
    
    return answer


for i in range(n):
    array_len = int(input())
    array = list(map(int, input().split()))
    print(solve(array_len, array))