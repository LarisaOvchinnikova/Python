year = input("Enter the year: ")
name = input("Enter the name: ")
file = open(f"babynamesranking{year}.txt")

for record in file:
    rank, boy_name, b_count, girl_name, g_count = record.split()
    if name == boy_name:
        print(f"{name} is ranked #{rank} in year {year}")
        print(f"{b_count} boys were named {name}")
        break
    if name == girl_name:
        print(f"{name} is ranked #{rank} in year {year}")
        print(f"{g_count} boys were named {name}")
        break

else:
    print(f"The name {name} is not ranked in year {year}")  # сработает
    # если цикл закончится сам по себе, без break, т.е имя не найдено


# ------
# for i in range(5):
#     if i > 3:
#         break
#     print(i)
# else:
#     print("end") # печатает только если цикл был закончен без break

