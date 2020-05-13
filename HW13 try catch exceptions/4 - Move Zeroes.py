# Given an array nums, write a function to move all 0's to the end
# of it while maintaining the relative order of the non-zero elements.

def move_zeros_to_end(arr):
    count_zeros = arr.count(0)
    while arr.count(0) != 0:
        arr.remove(0)
    for i in range(count_zeros):
        arr.append(0)
    return arr
print(move_zeros_to_end([0,1,0,3,12]))
