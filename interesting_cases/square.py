import math

n = [-5, -3, 0 , 1, 2, 3, 4, 5]
d_numbers = []
sorted_square_numbers = []

for i in range(len(n)):
    if n[i] > 0:
        pointer = 0
        while pointer <= len(d_numbers) - 1 and len(d_numbers) > 0:
            if d_numbers[pointer] ** 2 <= n[i] ** 2:
                sorted_square_numbers.append(d_numbers[pointer] ** 2)
                d_numbers.pop(pointer)
            else:
                pointer += 1
        sorted_square_numbers.append(n[i] ** 2)
    elif n[i] < 0:
        d_numbers.append(n[i])
    else:
        sorted_square_numbers.append(n[i]) 
    
print(sorted_square_numbers)