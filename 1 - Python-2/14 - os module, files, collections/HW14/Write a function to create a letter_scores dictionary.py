def letter_scores_dict(arr):
    scores = {}
    for el in arr:
        letters = el[1].replace(" ", "")
        for char in letters:
           scores[char] = el[0]
    return scores

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                       (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
print(letter_scores_dict(scrabble_scores))