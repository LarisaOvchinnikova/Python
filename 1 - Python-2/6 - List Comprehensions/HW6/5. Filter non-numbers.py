def filtered_list(lst):
    return [el for el in lst if type(el) == int]

arr1 = [1, False, 2, 'a', 'b', True]
arr2 = [1, 'a', None, 'b', None, 0, 15]
arr3 = [1, 2, True, 'aasf', '1', '123', 123]
print(filtered_list(arr1))
print(filtered_list(arr2))
print(filtered_list(arr3))