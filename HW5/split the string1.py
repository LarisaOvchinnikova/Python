def split_the_string_in_paragraphs(s):
    res = ''
    for i in range(0, len(s), 4):
        res = res + s[i: i+4] + "\n"
    return res

print(split_the_string_in_paragraphs("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
