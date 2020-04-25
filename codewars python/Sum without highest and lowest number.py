def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    sum = 0
    for el in arr:
        sum += el
    max1 = max(arr)
    min1 = min(arr)
    return sum - max1 - min1