def get_student_names(dct):
    arr = sorted(dct.values())
    return arr

print(get_student_names({
  "student_card_6733" : "Steve",
  "student_card_2343" : "Becky",
  "student_card_1239" : "John"
}))
