table = [
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-']
]

def draw():
    print("-" * 25)
    for row in table:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
        print("-" * 25)

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
        if row.count(row[1]) == 5 and row[1] != "-" and row[5] != row[1] or row.count(row[1]) == 5 and row[1] != "-" and row[0] != row[1]:
             print("The winner is player", row[1])
             return False

    for i in range(6):
        if table[0][i] == table[1][i] == table[2][i] == table[3][i] == table[4][i] and table[5][i] != table[0][i] and table[0][i] != '-' or table[1][i] == table[2][i] == table[3][i] == table[4][i] == table[5][i] and table[1][i] != table[0][i] and table[1][i] != '-':
            print("The winner is player", table[1][i])
            return False

    temp = [table[i][i] for i in range(6)]
    if temp.count(temp[1]) == 5 and temp[1] != temp[0] or temp.count(temp[1]) == 5 and temp[5] != temp[1]:
        print("The winner is player", row[1])
        return False

    if table[0][5] == table[1][4] == table[2][3] == table[3][2] == table[4][1] and table[4][1] != table[5][0] or table[1][4] == table[2][3] == table[3][2] == table[4][1] == table[5][0] and table[4][1] != table[0][5]:
        print("The winner is player", table[1][4])
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