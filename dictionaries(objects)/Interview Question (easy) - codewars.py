def get_strings(city):
    obj = {}
    city = list(city.lower())
    print(city)
    for el in city:
        if not el in obj:
            obj[el] = "*"
        else:
            obj[el] += "*"

    return list(obj)


print(get_strings("Chicago"))