# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1
def capitalize(s,ind):
    st = ''
    for i in range(len(s)):
        if i in ind:
            st = st + s[i].upper()
        else:
            st = st + s[i]
    return st