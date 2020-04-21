def words_in_column(text):
    arr = text.split()
    max = 0
    for el in arr:
        if len(el) > max:
            max = len(el)
    res = []
    for el in arr:
       res.append(el.rjust(max))
    return "\n".join(res)

text = "Shine on you crazy diamond"
print(words_in_column(text))