def common_letters(arr):
    s = set(arr[0])
    #print(s)
    for el in arr:
        s = s & set(el)
    common = "".join(s)
    return common
print(common_letters(["flower","flow","flight"]))
print(common_letters(["dog","racecar","car"]))
print(common_letters(['monkey', 'monday']))