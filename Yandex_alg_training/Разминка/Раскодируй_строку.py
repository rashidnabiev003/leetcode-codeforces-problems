


def main():
    answer = []
    n = int(input())
    nums = list(map(int, input().split()))
    prefix = [0]
    for i in range(n):
        prefix.append(nums[i] + prefix[i])
    
    for i in range(n):
        if nums[i]

    print(answer)
if __name__ == '__main__':
    main()