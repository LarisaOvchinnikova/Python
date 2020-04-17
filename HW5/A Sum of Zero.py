# returns True if the sum of two numbers in the list is zero
def check_sum(arr):
    n = 0
    for el in arr:
        if -el in arr:
            return True
    return False

print(check_sum([10, -14, 26, 5, -3, 13, -5]))

