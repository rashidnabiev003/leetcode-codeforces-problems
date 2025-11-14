n = int(input())
misha = 0
cris = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        misha += 1
    elif a < b:
        cris += 1

if misha > cris:
    print("Mishka")
elif cris > misha:
    print("Chris")
else:
    print("Friendship is magic!^^")