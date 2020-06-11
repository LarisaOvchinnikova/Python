def numbers_even_length(arr):
    return [el for el in arr if len(str(el)) % 2 == 0]


nums = [12, 345, 2, 6, 7896]
print(numbers_even_length(nums))