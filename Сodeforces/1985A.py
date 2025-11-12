words_count = int(input())

def replace(word_1, word_2):
    word_1 = list(word_1)
    word_2 = list(word_2)

    replacer = word_1[0]
    word_1[0] = word_2[0]
    word_2[0] = replacer
    return ''.join(word_1) + ' ' + ''.join(word_2)


for _ in range(words_count):
    word_1, word_2 = input().split()
    print(replace(word_1, word_2))
