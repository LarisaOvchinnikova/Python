from datetime import datetime
# Transform a string of 12-hour format to a 24-hour format with datetime
# "1:30 PM" => "13:30"
# "12:30 AM" => "00:30"
# strftime - переводим время из формата datetime в строку
time = "1:30 PM"
d = datetime.strptime(time, "%I:%M %p")
print(d)
time_24 = datetime.strftime()
# Transform a string of 24-hour format to a 12-hour format with datetime
# "14:30" => "2:30 PM"
# "11:30" => "11:30 AM"