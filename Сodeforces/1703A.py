n = int(input())

def yes(s):
    s = s.lower()
    if s == 'yes':
        return  "YES"
    else:
        return "NO"

for i in range(n):
    s = input()
    print(yes(s))