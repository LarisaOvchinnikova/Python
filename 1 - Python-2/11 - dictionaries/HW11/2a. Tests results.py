def results(arr):
    average = round(sum(arr) / len(arr), 3)
    grades = {}
    for grade in arr:
        if grade in [9, 10]:
            grades["h"] = grades.get("h", 0) + 1
        elif grade in [7, 8]:
            grades["a"] = grades.get("h", 0) + 11
        else:
            grades["l"] = grades.get("h", 0) + 11

    return [average, grades] + ["They did well"] * (len(arr) == grades["h"])

print(results([10, 9, 9, 10, 9, 10, 9]))
print(results([5, 6, 4, 8, 9, 8, 9, 10, 10, 10]))