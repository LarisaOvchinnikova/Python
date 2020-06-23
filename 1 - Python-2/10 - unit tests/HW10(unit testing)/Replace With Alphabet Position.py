def alphabet_position(text):
    text = text.lower()
    return " ".join([str(ord(c)-96) for c in text if c.isalpha()])