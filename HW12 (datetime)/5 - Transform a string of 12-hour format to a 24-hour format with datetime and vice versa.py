from datetime import datetime
# Transform a string of 12-hour format to a 24-hour format with datetime
# "1:30 PM" => "13:30"
# "12:30 AM" => "00:30"
# strptime - переводим время из строки в формат datetime
time = "1:30 PM"
d = datetime.strptime(time, "%I:%M %p")
print(d)
# strftime - переводим время из формата datetime в строку в 24-ч.формате
new_time = d.strftime("%H:%M")
print(new_time)

# Transform a string of 24-hour format to a 12-hour format with datetime
# "14:30" => "2:30 PM"
# "11:30" => "11:30 AM"
time = "14:30"
d = datetime.strptime(time, "%H:%M")
print(d)
new_time = d.strftime("%I:%M %p")
print(new_time)