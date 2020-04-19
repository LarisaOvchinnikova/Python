def multiply_even_number_by_ten(table):
    res = []
    for row in table:
        resRow = []
        for el in row:
            if el % 2 == 0:
                el *= 10
                resRow.append(el)
            else:
                resRow.append(el)
        res.append(resRow)
    return res
table = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
print(multiply_even_number_by_ten(table))