def remove_duplicate_words(s):
    arr = s.split(" ")
    res = []
    for el in arr:
        if not el in res:
            res.append(el)
    return " ".join(res)