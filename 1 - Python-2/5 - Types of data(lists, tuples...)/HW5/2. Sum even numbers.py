def sum_even(arr):
    return sum([el for el in arr if el % 2 == 0])


arr = [4,3,1,2,5,10,6,7,9,8]
print(sum_even(arr))