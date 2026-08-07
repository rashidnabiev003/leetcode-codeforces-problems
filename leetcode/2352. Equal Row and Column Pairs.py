grid = [[3,2,1],[1,7,6],[2,7,7]]

rows = {}
count = 0

for i in grid:
    c = tuple(i)
    if c in rows:
        rows[c] += 1
    else:
        rows[c] = 1

for i in range(len(grid)):
    k = []
    for j in range(len(grid[0])):
        k.append(grid[j][i])
    if tuple(k) in rows:
        count += rows[tuple(k)]

print(count)