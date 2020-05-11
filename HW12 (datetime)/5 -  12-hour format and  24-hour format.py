from datetime import datetime

today = datetime.today()
print(today)
time_in_12_format = today.strftime("%I:%M %p")  #12-hour clock
time_in_24_format = today.strftime("%H:%M")
print(time_in_12_format)  # "07:31 PM"
print(time_in_24_format)  # "19:53"

