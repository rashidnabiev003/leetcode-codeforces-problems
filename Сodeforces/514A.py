number = list(map(int, input()))

for i in range(len(number)):
    if i == 0 and number[i] == 9:
        continue
    elif number[i] >= 5:
        number[i] = 9 - number[i]

print(''.join(map(str, number)))