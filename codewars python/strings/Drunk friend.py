#https://www.codewars.com/kata/558ffec0f0584f24250000a0
def decode(string):
    if type(string) != str:
        return 'Input is not a string'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    s = ""
    for el in string:
        if el.lower() in alph:
            if el.islower():
                s += alph[25-alph.index(el.lower())]
            else:
                s += alph[25-alph.index(el.lower())].upper()
        else:
            s += el
    return s