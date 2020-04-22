#  Use list comprehension and range function
#  to create a list of numbers with type str

def createListOfNumbers(n):
    x = [str(number) for number in range(n)]
    return x
print(createListOfNumbers(10))