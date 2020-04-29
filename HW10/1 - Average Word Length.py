def average_word_length(arr):
    lst = [len(word) for word in arr]
    s = sum(lst) / len(lst)
    return round(s)

#lst = ["banana", "apple", "grape", "mom", "a"]
f = open("most_common_words.txt")
arr = f.read().split()
f.close()
print(average_word_length(arr))