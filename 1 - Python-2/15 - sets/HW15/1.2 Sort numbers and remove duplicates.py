def sorted_nums(arr):
    return sorted(set(arr), reverse=True)

arr = [1, 1, 2, 3, 5, 1, 9, 2]
print(sorted_nums(arr))