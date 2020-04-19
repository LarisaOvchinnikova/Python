def find_numbers_with_even_number_of_digits(nums):
    res = []
    for el in nums:
        x = len(str(el))
        if x % 2 == 0:
            res.append(el)
    return res

print(find_numbers_with_even_number_of_digits([12,345,2,6,7896]))
print(find_numbers_with_even_number_of_digits([555, 901, 482, 1771]))