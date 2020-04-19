def sum_even(arr):
    sum = 0
    for el in arr:
        if el % 2 == 0:
            sum += el
    return sum
arr = [4, 3, 1, 2, 5, 10, 6, 7, 9, 8]
print(sum_even(arr))