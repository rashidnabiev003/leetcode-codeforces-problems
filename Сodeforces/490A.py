numbers_count = int(input())
numbers = list(map(int, input().split()))
ones = []
twos = []
trees = []

for i in range(numbers_count):
    if numbers[i] == 1:
        ones.append(i + 1)
    elif numbers[i] == 2:
        twos.append(i + 1)
    else:
        trees.append(i + 1)

commands_count = min(min(len(ones), len(twos)),len(trees))
print(commands_count)
for i in range(commands_count):
    print(ones[i], twos[i], trees[i])