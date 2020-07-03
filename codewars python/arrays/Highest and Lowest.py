def high_and_low(numbers):
    arr = numbers.split(" ")
    arr = [int(el) for el in arr]
    arr = sorted(arr)
    return str(arr[-1]) + " " + str(arr[0])