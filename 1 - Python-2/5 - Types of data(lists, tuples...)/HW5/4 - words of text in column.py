def words_in_column(text):
    text = text.split()
    s = ""
    max_length = max([len(el) for el in text])
    for i, el in enumerate(text):
        if i != len(text) - 1:
            s += el.rjust(max_length)+'\n'
        else:
            s += el.rjust(max_length)
    return s

text = "Shine on you crazy diamond"
print(words_in_column(text))