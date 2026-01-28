#s = "A man, a plan, a canal: Panama"
s = "race a car"
s = s.lower()
clear_string = ''.join(filter(str.isalnum, s))
clear_string = list(clear_string)

left = 0
right = len(clear_string) - 1

while left <= right:
    if clear_string[left] == clear_string[right]:
        right -= 1
        left += 1
    elif clear_string[left] != clear_string[right]:
        print(False)
        break
    
print(True)