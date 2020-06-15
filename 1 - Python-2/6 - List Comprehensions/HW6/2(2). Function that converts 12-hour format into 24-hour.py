def get_military_time(us_time):
    time = us_time[-2:]
    minutes = us_time[3:5]
    hour = int(us_time[0:2])
    if time == "PM":
        if hour != 12:
            hour = hour + 12
        elif hour == 12:
            hour = 0
    hour = str(hour)
    if len(hour) < 2:
        hour = "0" + hour
    milTime = hour + ":" + minutes
    return milTime


print((get_military_time("07:05 PM")))
print((get_military_time("07:05 AM")))
print((get_military_time("12:05 AM")))
print((get_military_time("12:05 PM")))

