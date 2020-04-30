def count_animals(s):
    lst = s.split()
    sum = 0
    for el in lst:
        if el.isdigit():
            sum = sum + int(el)
    return sum