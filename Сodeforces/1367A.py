n = int(input())

def solve(s):
    if len(s) <= 2:
        return s
    final_string = []
    final_string = [s[x] for x in range(len(s)) if x % 2 == 0] 
    final_string.append(s[-1])
    return final_string

for _ in range(n):
    print(*solve(list(input())), sep="")