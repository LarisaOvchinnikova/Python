def average_word_length(arr):
    lst = [len(word) for word in arr]
    print(lst)
    s = sum(lst) / len(lst)
    return round(s,2)


# lst = ["banana", "apple", "grape", "mom", "a"]


f = open("most_common_words.txt")
lst = f.read().split()
f.close()

print(average_word_length(lst))