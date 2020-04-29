def average_word_length(arr):
    lst = [len(word) for word in arr]
    s = sum(lst) / len(lst)
    return s

lst = ["banana", "apple", "grape", "mom", "a"]
print(average_word_length(lst))