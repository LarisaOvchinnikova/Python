def accum(s):
    s1 = ""
    for i in range(len(s)):
        s1 = s1 + s[i].upper() + s[i].lower() * i + "-"
    return s1[:-1]