https://www.codewars.com/kata/55c11989e13716e35f000013
def add(a,b):
    l = max(len(a), len(b))
    a = a.rjust(l,"0")
    b = b.rjust(l,"0")
    s = ""
    p = 0
    for i in range(l-1, -1, -1):
        el = a[i] + b[i]
        if el == "01" and p == 0:
            s = "1" + s
            p = 0
        elif el == "10" and p == 0:
            s = "1" + s
            p = 0
        elif el == "00" and p == 0:
            s = "0" + s
            p = 0
        elif el == "11" and p == 0:
            s = "0" + s
            p = 1
        elif el == "01" and p == 1:
            s = "0" + s
            p = 1
        elif el == "10" and p == 1:
            s = "0" + s
            p = 1
        elif el == "00" and p == 1:
            s = "1" + s
            p = 0
        elif el == "11" and p == 1:
            s = "1" + s
            p = 1
    if p == 1:
        s = "1" + s
    else:
        s = s.lstrip("0")
    return s if s else "0"