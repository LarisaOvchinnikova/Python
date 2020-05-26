def divide(a, b):
    try:
        result = a/b
        if result < 0:
            raise ValueError("Cannot be negative")
        return result
    except ZeroDivisionError as err:
        print(err)
        return 0


print(divide(10, 0))