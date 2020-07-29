# import itertools
# arr = [[1,2], [3,5], [6, 7], [9,[10, 11]]]
#merged = list(itertools.chain.from_iterable(arr))
# print(merged)

# def flatten(arr):
#     flat = []
#     for el in arr:
#         flat += el
#     return flat

# print(flatten(arr))

def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])
s=[[1,2],[3,4, [2,4,[5]]]]
print("Flattened list is: ",flatten(s))