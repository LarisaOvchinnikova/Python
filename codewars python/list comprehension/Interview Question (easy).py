https://www.codewars.com/kata/5b358a1e228d316283001892
def get_strings(city):
    city = city.lower().replace(" ", "")
    a = []
    for el in city:
        if el not in a:
            a.append(el)
    return ",".join([f'{el}:{"*"*city.count(el)}' for el in a])