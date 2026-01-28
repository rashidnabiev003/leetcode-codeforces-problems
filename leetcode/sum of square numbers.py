import math
c = 8
l = 0 
r = int(math.sqrt(c))

while l <= r:
    total = l ** 2 + r ** 2
    if total == c:
        print(True)
        break
    elif total < c:
        l += 1
    else:
        r -= 1
print(False)