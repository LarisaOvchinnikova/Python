# https://www.codewars.com/kata/541629460b198da04e000bb9/

def last(*arr):
    if type(arr[-1]) in [str, list]:
        return arr[-1][-1]
    return arr[-1]