s = 0
count = 0
while True:
    number = input("Enter a number: ")
    if number.lower() == "exit":
        break
    s += int(number)
    count += 1
aver = round(s / count, 1)
print(f"Okay user...\nYou have entered {count} numbers and the average value is {aver}")

