# Given an array of integers arr,
# write a function that returns true if and only if the number
# of occurrences of each value in the array is unique.
def  occurences(arr):
    s = set(arr)
    #print(s)
    un_el = list(s)
    #print(un_el)
    lst = [arr.count(el) for el in un_el]
    #print(lst)
    return len(set(lst)) == len(lst)


print(occurences([1,2,2,1,1,3]))
print(occurences([1,2]))
print(occurences([-3,0,1,-3,1,1,1,-3,10,0]))