from datetime import datetime
# Transform a string of 12-hour format to a 24-hour format with datetime
# "1:30 PM" => "13:30"
# "12:30 AM" => "00:30"
# strftime - переводим время из формата datetime в строку
today = datetime.today()
print(today)
time_in_12_format = today.strftime("%I:%M %p")  #12-hour clock
time_in_24_format = today.strftime("%H:%M")
print(time_in_12_format)  # "07:31 PM"
print(time_in_24_format)  # "19:53"

# Transform a string of 24-hour format to a 12-hour format with datetime
# "14:30" => "2:30 PM"
# "11:30" => "11:30 AM"