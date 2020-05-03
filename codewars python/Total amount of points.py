def points(games):
    s = 0
    for el in games:
        if int(el[0]) > int(el[2]):
            s += 3
        elif int(el[0]) == int(el[2]):
            s += 1
    return s