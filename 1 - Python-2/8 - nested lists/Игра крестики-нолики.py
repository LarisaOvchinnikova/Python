table = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def draw():
    # """TODO: Draw table
    #  -------------
    #  | - | - | - |
    #  -------------
    #  | - | - | - |
    #  -------------
    #  | - | - | - |
    #  -------------
    #  """
    print("-" * 13)
    for row in table:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
        print("-" * 13)


def get_point(value):
    """ TODO:
    ask to input row and column
    If point is valid, place the value
    otherwise try again
    """
    point = input("Enter row and column number: ").split()
    row, col = [int(x) - 1 for x in point]

    while table[row][col] != "-":
        print("Wrong cell! Try another one!")
        point = input("Enter row and column number: ").split()
        row, col = [int(x) - 1 for x in point]

    table[row][col] = value
 #   return table

draw()
get_point("X")
draw()
get_point("O")
draw()


def check_winner():
    """ TODO:
    if there is no winner return True
    otherwise print who won and return False"""
    for row in table:
        if row.count(row[0]) == 3 and row[0] != "-":
            print("The winner is player", row[0])
            return False

    for i in range (3):
        if table[0][i] == table[1][i] == table[2][i] and table[0][i] != "-":
            print("The winner is player", table[0][i])
            return False

    temp = [table[i][i] for i in range(3)]
    if temp.count(temp[0] == 3 and temp[0] != "-"):
        print("The winner is player", row[0])
        return False

    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != '-':
        print("The winner is player", table[0][2])
        return False

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