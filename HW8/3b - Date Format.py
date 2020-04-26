# Create a function that takes 3 integers: date, month, year and
# returns in a string format.
# # Think how you can do this without 12 if statements

def format_date(date, month, year):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                  "December"]
    month = month_list[month - 1]
    dct = {}
    for count, m in enumerate(month_list):
        dct[m] = count + 1

    return dct


print(format_date(5, 5, 1789))
print(format_date(28, 7, 1914))
print(format_date(29, 8, 1997))
