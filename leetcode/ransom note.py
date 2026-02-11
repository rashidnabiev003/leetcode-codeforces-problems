ransomNote = "a"
magazine = "a"
dictionary = {}


for i in magazine:
    if dictionary.get(i) is None:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for i in ransomNote:
    if dictionary.get(i) is not None:
        dictionary[i] -= 1
        if dictionary[i] < 0:
            print(False)
            break
    else:
        print(False)
        break

print(True)
         

