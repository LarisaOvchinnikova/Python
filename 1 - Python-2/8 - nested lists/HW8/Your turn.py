table = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]

def draw():
    print("-" * 21)
    for row in table:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
        print("-" * 21)

def get_point(value):
    point = input("Enter row and column number: ").split()
    row, col = [int(x) - 1 for x in point]

    while table[row][col] != "-":
        print("Wrong cell! Try another one!")
        point = input("Enter row and column number: ").split()
        row, col = [int(x) - 1 for x in point]

    table[row][col] = value

def check_winner():

    for row in table:
        if row.count(row[0]) == 5 and row[0] != "-":
            print("The winner is player", row[0])
            return False

    for i in range (5):
        if table[0][i] == table[1][i] == table[2][i] == table[3][i] == table[4][i] and table[0][i] != "-":
            print("The winner is player", table[0][i])
            return False

    temp = [table[i][i] for i in range(5)]
    if temp.count(temp[0] == 5 and temp[0] != "-"):
        print("The winner is player", row[0])
        return False

    if table[0][4] == table[1][3] == table[2][2] == table[3][1] == table[4][0] and table[0][4] != '-':
        print("The winner is player", table[0][4])
        return False

    return True

def check_draw():
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