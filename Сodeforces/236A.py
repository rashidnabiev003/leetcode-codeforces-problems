from collections import Counter
 
b = list(input())
b = Counter(b).keys()
if len(b)%2 != 0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')