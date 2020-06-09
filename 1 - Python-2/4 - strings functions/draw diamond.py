def draw_diamond(rows):
    width = rows * 2 - 1
    s = ""
    for i in range(1, rows * 2, 2):
        s = s + ("*"*i).center(width) + "\n"
    for i in range(rows * 2 - 3, 0, -2):
        s = s + ("*"*i).center(width) + "\n"
    return s

print(draw_diamond(7))