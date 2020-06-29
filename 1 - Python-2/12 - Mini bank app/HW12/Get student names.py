# def get_student_names(dct):
#     return sorted([value for value in dct.values()])

def get_student_names(dct):
    return sorted(list(dct.values()))


def get_student_names(dct):
  return sorted(dct.values())


print(get_student_names({
  "student_card_6733" : "Steve",
  "student_card_2343" : "Becky",
  "student_card_1239" : "John"
}))

print(get_student_names({
  "student_card_6733" : "Steve",
  "student_card_2343" : "Becky",
  "student_card_1239" : "John"
}))