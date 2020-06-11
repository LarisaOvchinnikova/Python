def middle_of_list(lst):
    n = len(lst)
    if n % 3 != 0:
        return "Error"
    middle = lst[n//3: n//3 + n//3][::-1]
    return middle

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(middle_of_list(input))