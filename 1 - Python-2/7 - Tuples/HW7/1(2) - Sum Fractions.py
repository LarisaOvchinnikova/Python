def sum_fractions(arr):
    return round(sum([el[0] / el[1] for el in arr]))


def sum_fr(arr):
    return round(sum([numerator/denominator for numerator, denominator in arr]))




print(sum_fractions([[18, 13], [4, 5]]))
# print(sum_fractions([[36, 4], [22, 60]]))
# print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))

print(sum_fr([[18,13], [4,5]]))