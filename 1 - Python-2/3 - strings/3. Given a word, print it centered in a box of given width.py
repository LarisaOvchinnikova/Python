def word_in_box(word, width):
    s = "*"
    if width < len(word):
        return "ERROR"
    else:
        return f"{s * width}\n*{word.center(width - 2)}*\n{s * width}"


print(word_in_box("Possum", 30))