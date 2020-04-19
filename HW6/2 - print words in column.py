def words_in_column(text):
    arr = text.split()
    l = []
    res = ''
    for el in arr:
        l.append(len(el))
    m = max(l)
    for i, el in enumerate(arr):
        if i != len(arr) - 1:
            res = res + el.rjust(m) + '\n'
        else:
            res = res + el.rjust(m)
    return res
text = "Shine on you crazy diamond"
print(words_in_column(text))