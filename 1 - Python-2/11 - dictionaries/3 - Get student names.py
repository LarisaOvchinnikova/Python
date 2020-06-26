def get_student_names(dct):
    arr = []
    for value in dct.values():
       # print(value)
        arr.append(value)
    arr.sort()
    return arr

print(get_student_names({
  "student_card_6733" : "Steve",
  "student_card_2343" : "Becky",
  "student_card_1239" : "John"
}))
