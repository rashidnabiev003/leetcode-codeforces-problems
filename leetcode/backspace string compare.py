s = "ab#c"
t = "ad#casdasd"

def clear(string):
    clear_string = []
    string = list(string)
    read_pointer = 0
    while read_pointer <= len(string) - 1:
        if string[read_pointer] != '#':
            clear_string .append(string[read_pointer])
            read_pointer += 1
        elif len(clear_string) > 0: 
            clear_string.pop()
            read_pointer += 1
        else:
            read_pointer += 1
    return ''.join(filter(str, clear_string))

print(True) if clear(s) ==  clear(t) else print(False)
