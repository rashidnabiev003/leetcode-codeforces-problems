n = input()
array = list(n)
number = int(n)
if number >= 0:
    print(n)
else:
    array.remove('-')
    array = list(map(int, array))
    if len(array) > 1:
        if array[-1] > array[-2]:
            array.pop(-1)
        else:
            array.pop(-2)
        print('-', *array, sep='') if array[0] != 0 else print(0)
    else:
        print(0)