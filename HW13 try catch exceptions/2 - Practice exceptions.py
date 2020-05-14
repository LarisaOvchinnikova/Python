def positive_divide(a, b):

    try:
        result = a / b
        if result < 0:
            raise ValueError("Cannot be negative")
        return result
    except ZeroDivisionError:
        return 0
    except TypeError as error:
        return "Type Error!!!!!!"
        print(error)

# print(positive_divide(1, 2)) # ---> 0.5
print(positive_divide(1, 0)) # ---> 0
# print(positive_divide(2, 0)) # ----> 0
# print(positive_divide(1, 's')) # ---> TypeError
# print(positive_divide([], 2)) # ---> TypeError
print(positive_divide(1, -2)) # ----> ValueError('Cannot be negative')
print(positive_divide(-1, 2)) # ---> ValueError('Cannot be negative')