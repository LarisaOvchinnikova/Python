def flatten(arr):
    result = []
    for elem in arr:
        if type(elem) in [list, tuple]:
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
print(list(flatten(x)))