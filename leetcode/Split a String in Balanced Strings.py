s = "RLLLLRRRLR"
fin_count = 0
char_count = 0
previous = s[0]

for i in s:
    if i == previous or previous == '':
        char_count += 1
        previous = i
    if i != previous:
        char_count -= 1
        if char_count <= 0:
            fin_count += 1
            previous = ''

print(fin_count)
        


