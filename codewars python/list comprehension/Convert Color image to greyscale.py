# https://www.codewars.com/kata/590ee3c979ae8923bf00095b
def color_2_grey(colors):
    res = []
    for el in colors:
        arr = [[round(sum(el1)/3)] * 3 for el1 in el]
        res.append(arr)
    return res

# 2 case
def color_2_grey(colors):
    return [[[round(sum(el1)/3)] * 3 for el1 in el] for el in colors]