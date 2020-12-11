# https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b
def split_integer(num, parts):
    n = num / parts
    if int(n) == n:
        return [n] * parts
    else:
        n1 = int(n)
        n2 = n1+1
        for i in range(parts+1):
            for j in range(parts+1):
                if n1 * i + n2 * j == num and i + j == parts:
                    return [n1] * i + [n2] * j