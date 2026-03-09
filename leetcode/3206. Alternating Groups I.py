colors = [1, 1, 1]
groups_count = 0

for i in range(len(colors)):
    if i == 0:
        if (colors[-1] == colors[i + 1]) and colors[-1] != colors[i]:
            groups_count += 1
    elif i == len(colors) - 1:
        if (colors[0] == colors[i - 1]) and colors[0] != colors[i]:
            groups_count += 1
    else:
        if (colors[i - 1] == colors[i + 1]) and colors[i - 1] != colors[i]:
            groups_count += 1

print(groups_count)
