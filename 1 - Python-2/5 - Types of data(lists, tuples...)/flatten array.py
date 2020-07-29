def flatten(arr):
    result = []
    for elem in arr:
        if type(elem) in [list, tuple]:
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
print(list(flatten(x)))
# 2 case^
# x = ['a', 'b', ['c', 'd', [[0, "1", ["3"]]]]]
# def flatten(arr):
#     for elem in arr:
#         if type(elem) in [list, tuple]:
#             yield from flatten(elem)
#         else:
#             yield elem
# print(list(flatten(x)))

# yield from будет возвращать по одному элементу из списка