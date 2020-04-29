def letter_scores_dict(arr):
    dct = {}
    for el in arr:
        #print(el[0])
        print(el[1])
        letters = el[1].split()
        print(letters)
        for symb in letters:
            dct[symb] = el[0]
    return dct

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                       (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
print(letter_scores_dict(scrabble_scores))
