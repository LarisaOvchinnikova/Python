def align_text(text):
    text = text.split()
    length_list = [len(el) for el in text]
    longest = max(length_list)
    new_text = [el.rjust(longest) for el in text]
    return "\n".join(new_text)

text = "Shine on you crazy diamond"
words = align_text(text)
print(words)
