def newtest(r):
    average = round(sum(r) / len(r), 3)
    dct = {
        "h": 0,
        "a": 0,
        "l": 0
    }
    for el in r:
        if el >= 9:
            dct["h"] += 1
        elif el >= 7:
            dct["a"] += 1
        else:
            dct["l"] += 1

    if dct["a"] + dct["l"] == 0:
        return [average, dct, "They did well"]
    else:
        return [average, dct]



print(newtest([10, 9, 9, 10, 9, 10, 9]))
print(newtest([5, 6, 4, 8, 9, 8, 9, 10, 10, 10]))