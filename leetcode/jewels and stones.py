jewels = "aA"
stones = "aAAbbbb"
s = {x:0 for x in jewels}
iter = 0

for i in stones:
    if s.get(i) is not None:
        iter += 1

print(iter)