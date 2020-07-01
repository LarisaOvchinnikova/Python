table = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def draw():
    #  Draw table
    #  -------------
    #  | - | - | - |
    #  -------------
    #  | - | - | - |
    #  -------------
    #  | - | - | - |
    #  -------------

    print("-" * 13)
    for row in table:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
        print("-" * 13)


def get_point(value):
    while True:
        point = input("Enter row and column number: ").split()
        if len(point) != 2:
            print("You need to enter two digits")
            continue

        row, col = point
        if not (row.isdigit() and col.isdigit()):
            continue

        row, col = [int(x) - 1 for x in point]
        if not (0 <= row < len(table) and 0 <= col < len(table)):
            continue

        if table[row][col] != "-":
            continue

        table[row][col] = value
        break



def check_winner():
    # horizontal rows:
    for row in table:
        if row.count(row[0]) == 3 and row[0] != "-":
            print("The winner is player", row[0])
            return False

    # vertical columns:
    for i in range(len(table)):
        temp = [table[j][i] for j in range(len(table))]
        if temp.count(temp[0]) == len(table) and temp[0] != "-":
           print("The winner is player", temp[0])
           return False

    # main diagonal:
    temp = [table[i][i] for i in range(len(table))]
    if temp.count(temp[0]) == len(table) and temp[0] != "-":
        print("The winner is player", temp[0])
        return False

    # second diagonal:
    temp = [table[i][len(table) - i - 1] for i in range(len(table))]
    if temp.count(temp[0]) == len(table) and temp[0] != "-":
        print("The winner is player", temp[0])
        return False
    # if table[0][2] == table[1][1] == table[2][0] and table[0][2] != '-':
    #     print("The winner is player", table[0][2])
    #     return False

    return True

def check_draw():
    """ TODO:
    if draw print "Draw!" and return False,
    otherwise return True"""
    for row in table:
        for cell in row:
            if cell == "-":
                return True
    print("It is Draw!")
    return False

def play():
    player = "X"
    while check_winner() and check_draw():
        draw()
        get_point(player)
        if player == "X":
            player = "O"
        else:
            player = "X"
    draw()


play()