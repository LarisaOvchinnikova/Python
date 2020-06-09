def get_strings(city):
    obj = {}
    city = list(city.lower())
    s = ''
    for el in city:
        if not el in obj:
            obj[el] = "*"
        else:
            obj[el] += "*"

    for keys  in obj:
        print(keys, obj[keys])
        s = s + f"{keys}:{obj[keys]},"
    return s[:-1]

print(get_strings("Chicago"))