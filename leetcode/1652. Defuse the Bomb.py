code = [5,7,1,4]
k = 3
n = len(code)

result = [0] * n

if k == 0:
    print(result)

if k > 0:
    start, end = 1, k
else:
    start, end = n + k, n - 1 

window_sum = sum(code[i % n] for i in range(start, end + 1))
result[0] = window_sum

for i in range(1, n):
    window_sum -= code[start % n]
    start = (start + 1) % n
    end = (end + 1) % n
    window_sum += code[end % n]
    
    result[i] = window_sum

print(result)