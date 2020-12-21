# https://www.codewars.com/kata/5a15a5d557f0af795b00005f
def encrypt(s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alph[25 - alph.index(el)] for el in s])