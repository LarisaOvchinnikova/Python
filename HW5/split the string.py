def split_the_string_in_paragraphs(s):
    res = ''
    for i in range(len(s)):
        if  i % 4 == 3:
            res = res + s[i] + '\n'
        else:
            res = res + s[i]
    return res

print(split_the_string_in_paragraphs("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
