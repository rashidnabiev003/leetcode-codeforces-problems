s = "the sky is          blue    "
s = list(map(str, s.split(" ")))

def delete(s):
    new_string = []
    if len(s) < 2:
        return s
    for i in s:
        if i != '' and i != ' ':
            new_string.append(i)

    return new_string
s = delete(s)

print(' '.join(map(str, s[::-1])))