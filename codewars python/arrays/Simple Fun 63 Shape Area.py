def shape_area(n):
    res = [0,1]
    for i in range (2, n+1):
        res.append(res[i-1] + 4 + (i - 2) * 4)
    return res[n]