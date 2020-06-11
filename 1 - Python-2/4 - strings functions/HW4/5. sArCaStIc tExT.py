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

# ---- 2 case
def sarcastic(text):
    s = ''
    for i in range(len(text)):
        if i % 2 != 0:
            s += text[i].upper()
        else:
            s += text[i]
    return s

# --- 2 case
def sarcastic(text):
    return "".join([el if i % 2 == 0 else el.upper() for i, el in enumerate(text)])

text = "the earth is flat"
print(sarcastic(text))

# --- 3 case ---
def sarcastic(text):
    s = ''
    for i, letter in enumerate(text):
        if i % 2 != 0:
            s += letter.upper()
        else:
            s += letter
    return s