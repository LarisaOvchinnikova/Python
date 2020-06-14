# def even_digits(numbers):
#     new_lst = []
#     for num in numbers:
#         if len(str(num)) % 2 == 0:
#             new_lst.append(num)
#     return new_lst

def even_digits(numbers):
    return [el for el in numbers if len(str(numbers)) % 2 == 0]

nums = [55,901,482,1771]
print(even_digits(nums))