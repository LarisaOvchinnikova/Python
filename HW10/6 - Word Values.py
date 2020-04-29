def calc_word_value(word):
    word = word.upper()
    letter_scores = {'E': 1, 'A': 1, 'O': 1, 'I': 1, 'N': 1,
                     'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                     'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4,
                     'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
    s = 0
    for letter in word:
        # print(letter)
        # print(letter_scores[letter])
        s += letter_scores[letter]
    return s


def max_word_value(list_of_words):
    dct = {}
    for w in list_of_words[:80000]:
        #print(w)
        #print(calc_word_value(w))
        dct[w] = calc_word_value(w)


    return max(dct.values())



f = open("full_dictionary.txt")
words = f.read().split()
print(len(words))
f.close()
print(max_word_value(words))
# print(calc_word_value("fly"))
#print(calc_word_value("barbeque"))
