# дано число. вывести цифры, которых нет в этом числе
# n = 34885678   ---> 0,1,2,9
n = input("Enter your number: ")
n = set(n)
digits = set('1234567890')
res = ", ".join(digits - n)
print("Absent digits in your number:", res)