def middleOfList(input):
    k = len(input)
    if k % 3 != 0:
        return "Error"
    else:
        p = int(k / 3)   # p = k // 3
        middle = input[p: -p]
        return middle[::-1]
        # return input[p: p+p][::-1]
print(middleOfList([1,2,3,4,5,6,7,8, 9]))
