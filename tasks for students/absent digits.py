# дано число. вывести цифры, которых нет в этом числе
# n = 34885678   ---> 0,1,2,9
n = input("Enter your number: ")
n = str(n)
digits = '1234567890'
setn = set(n)
setdigits = set(digits)
absent = setdigits - setn
lst = sorted(list(absent))

print("Absent digits in your number:", lst)
res = ", ".join(lst)

print("Absent digits in your number:", res)