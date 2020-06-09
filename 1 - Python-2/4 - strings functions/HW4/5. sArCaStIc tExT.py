def sarcastic(text):
    s = ''
    for i in range(len(text)):
        if i % 2 != 0:
            s += text[i].upper()
        else:
            s += text[i]
    return s

text = "the earth is flat"
print(sarcastic(text))