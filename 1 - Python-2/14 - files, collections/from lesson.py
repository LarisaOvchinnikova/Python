from collections import Counter

items = ["a", "a", "b", "c", 'e']

count = Counter(items)
print(count)  # Counter({'a': 2, 'b': 1, 'c': 1, 'e': 1})
print(type(count))  # <class 'collections.Counter'>

items1 = ["a", "a", "b", "c", 'e']
items2 = ["b", "c", "e"]
count1 = Counter(items1)
count2 = Counter(items2)
print(count1)
print(count2)
print(count1 + count2)

# 3 самых популярных элемента
print(count1.most_common(3))  #[('a', 2), ('b', 1), ('c', 1)]


