asteroids = [3,5,-6,2,-1,4]
stack = []

for asteroid in asteroids:
    alive = True

    while stack and stack[-1] > 0 and asteroid < 0:
        if stack[-1] > abs(asteroid):
            alive = False
            break
        if stack[-1] == abs(asteroid):
            alive = False
            stack.pop()
            break
        if stack[-1] < abs(asteroid):
            stack.pop()
        
    if alive:
        stack.append(asteroid)

print(stack)