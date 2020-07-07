def letter_scores_dict(arr):
    # 1 вариант
    # scores = {}
    # for el in arr:
    #     letters = el[1].replace(" ", "")
    #     for char in letters:
    #        scores[char] = el[0]

    # 2 вариант
    # for score, letters in arr:
    #     for letter in letters.split():
    #         scores[letter] = score

    # 3 вариант
    scores = {letter: score for score, letters in arr for letter in letters.split()}
    return scores

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                       (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
print(letter_scores_dict(scrabble_scores))