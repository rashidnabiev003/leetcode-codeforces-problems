t = int(input())

for i in range(t):
    numbers = list(input())
    if int(numbers[0]) + int(numbers[1]) + int(numbers[2]) == int(numbers[-1]) + int(numbers[-2]) + int(numbers[-3]):
        print("YES")
    else:
        print("NO")