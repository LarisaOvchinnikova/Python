# If you can't sleep, just count sheep!!
# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    s = ''
    i = 1
    while i <= n:
        s = s + str(i) + " sheep..."
        i = i + 1
    return s

