# https://www.codewars.com/kata/58539230879867a8cd00011c
def find_children(s):
    if s == "" : return ""
    s = sorted(s.lower())
    t = ''
    for el in s:
        if t =='' or t[-1] == el:
            t += el
        else:
            t += " "+ el
    return t.title().replace(' ', '')