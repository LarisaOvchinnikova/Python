# https://www.codewars.com/kata/5e9c06f95ea5b30033903194
def how_bigga_ma_pizza(blob, crust):
    r = blob / 2
    return (4 * r ** 3 / 3) ** 0.5 if crust == "crispy" else  (4 * r ** 3 / 15) ** 0.5