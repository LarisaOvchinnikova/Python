def sum_fractions(fraction):
    s = 0
    for el in fraction:
        s = s + el[0] / el[1]
    return round(s)

print(sum_fractions([[18, 13], [4, 5]]))
print(sum_fractions([[36, 4], [22, 60]]))
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))