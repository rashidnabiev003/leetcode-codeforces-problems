from collections import Counter
s = "aaabb"
k = 3

def recursive(string):
    char_counter = Counter(string)
    for key, value in char_counter.items():
        if value < k:
            substrings = string.split(key)
            return max(recursive(string) for string in substrings)
    
    return len(string)

print(recursive(s))

            


