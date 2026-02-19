def divisorSubstrings(num: int, k: int) -> int:
    str_num = str(num)
    beauty_count = 0
    i = 0
    while i <= len(str_num) - k:
        if int(str_num[i:k + i]) != 0:
            if num % int(str_num[i:k + i]) == 0:
                beauty_count += 1
        i += 1
    return beauty_count

print(divisorSubstrings(num = 430043, k = 2))