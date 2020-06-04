name = input("Enter your name: ")
time = int(input("What's the time now? "))
if  0<= time <= 6:
    print(f"Good night, {name}")
elif 7 <= time <= 11:
    print(f"Good morning, {name}")
elif 12 <= time <= 17:
    print(f"Good day, {name}")
elif 18 <= time <= 23:
    print(f"Good evening, {name}")
else:
    print("Wrong time")