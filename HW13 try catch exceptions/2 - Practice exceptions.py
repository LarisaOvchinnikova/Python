def positive_divide(a, b):

    try:
        res = a / b
        return a / b
    except ZeroDivisionError as error:
        #print(error)
        return 0
    except TypeError as error:
        #print(error)
        return "Type Error!!!!!!"
        print(error)
    except ValueError:
        #if a < 0 or b < 0:
        #print("Cannot be negative")
        return "Cannot be negative"
    # except Exception as error:
    #     print(error)

    #finally:
        #print("I still work")


print(positive_divide(1, 2)) # ---> 0.5
print(positive_divide(1, 0)) # ---> 0
print(positive_divide(2, 0)) # ----> 0
print(positive_divide(1, 's')) # ---> TypeError
print(positive_divide([], 2)) # ---> TypeError
print(positive_divide(1, -2)) # ----> ValueError('Cannot be negative')
print(positive_divide(-1, 2)) # ---> ValueError('Cannot be negative')