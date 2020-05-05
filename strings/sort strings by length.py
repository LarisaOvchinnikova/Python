def sort_strings(arr):
    arr.sort(key=len)
    print(arr)

print(sort_strings(["pineapple", "bread", "juice", "cake", "mum", "banana", "a"]))