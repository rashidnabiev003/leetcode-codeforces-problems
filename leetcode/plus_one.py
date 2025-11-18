n = [4,3,2,1]
k = [9,9]

def plusOne(digits):
        z_flag = False
        pointer = len(digits) - 1
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        while 0 <= pointer or z_flag == True:
            if digits[pointer] + 1 > 9:
                z_flag = True
                digits[pointer] = 0
            elif pointer < 0 and z_flag == True:
                digits.append(1)
                return list(reversed(digits))
            else:
                digits[pointer] += 1
                return digits
            pointer -= 1
        return digits

print(plusOne(k))