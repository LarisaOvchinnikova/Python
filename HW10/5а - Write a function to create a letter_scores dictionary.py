def letter_scores_dict(arr):
    dct = {}
    for num, letters in arr:
        for symb in letters.split():
           dct[symb] = num
    return dct

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                       (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
print(letter_scores_dict(scrabble_scores))
