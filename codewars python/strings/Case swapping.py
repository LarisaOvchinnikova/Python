def swap(string_):
    s = ""
    for i in string_:
        if i == i.upper():
            s = s + i.lower()
        else:
             s = s + i.upper()
    return s

# ---2 case
def swap(string):
    return string.swapcase()