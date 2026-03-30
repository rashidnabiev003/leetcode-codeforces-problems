n = int(input())
for i in range(n):
    dictionary = {}
    matrix = int(input())
    for j in range(matrix):
        nums = list(map(int, input().split()))
        for x in nums:
            dictionary[x] = dictionary.get(x, 0) + 1

    for key, value in dictionary.items():
        if value > matrix*(matrix-1):
            print("NO")
            break
    else:
        print("YES")
        

