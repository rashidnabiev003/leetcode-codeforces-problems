
n = 9
numbers = [2,7,11,15]

def twoSum(numbers, target):
        dictionary = {}
        pointer = 0
        while pointer <= len(numbers) - 1:
            if dictionary.get(target - numbers[pointer]) is not None:
                return [dictionary[target - numbers[pointer]] + 1, pointer + 1]
            else:
                dictionary[numbers[pointer]] = pointer
            pointer += 1

print(twoSum(numbers=numbers, target=n))