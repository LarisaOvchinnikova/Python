def diff(a, b):
    setA = set(a)
    setB = set(b)
    dif1 = setA - setB
    dif2 = setB - setA
    return sorted(list(dif1 | dif2))