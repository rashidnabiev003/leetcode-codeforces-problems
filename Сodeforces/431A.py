array = list(map(int, input().split()))
index = [x for x in range(1, len(array) + 1)]
calory_dict = dict(zip(index, array))
calory_count = 0

s = list(map(int, input().strip()))

for i in range(len(s)):
    calory_count += calory_dict[s[i]]

print(calory_count)