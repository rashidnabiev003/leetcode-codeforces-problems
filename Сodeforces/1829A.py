n = int(input())
real = 'codeforces' 

def solve(string: str) -> str:
    diff_count = 0
    for i in range(len(string)):
        if list(string)[i] != list(real)[i]:
            diff_count += 1

    return diff_count

for _ in range(n):
    print(solve(input()))