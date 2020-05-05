def final_grade(s1,s2,s3):
    if s1.isdigit() and s2.isdigit() and s3.isdigit():
        print("ok")
    else:
        print("wrong test grade")
    s1, s2, s3 = int(s1), int(s2), int(s3)
    average = (s1+s2+s3)/3
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(final_grade('80','90','100'))