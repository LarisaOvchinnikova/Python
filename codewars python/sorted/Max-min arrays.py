#https://www.codewars.com/kata/5a090c4e697598d0b9000004
def solve(arr):
    arr = sorted(arr)
    print(arr)
    res = []
    while len(arr)>0:
        res.append(arr[-1])
        arr.pop()
        if len(arr) == 0:
            break
        else:
            res.append(arr[0])
            del arr[0]
    return res