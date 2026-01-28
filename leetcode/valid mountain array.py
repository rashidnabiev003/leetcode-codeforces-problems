arr = [1,3,2]
array_len = len(arr) - 1
l = 0
r = 1
neg_flag = False

if array_len - 1 <= 2:
    #return False
    pass

while r <= array_len:
    if arr[l] < arr[r] and neg_flag is False:
        r += 1
        l += 1
    elif l == 0 and arr[l] > arr[r]:
        #return False
        print(False)
        break
    elif arr[l] > arr[r]:
        r += 1
        l += 1
        neg_flag = True
    else:
        #return False
        print(False)
        break

print(True if neg_flag is True else False)