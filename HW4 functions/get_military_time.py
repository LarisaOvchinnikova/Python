def get_military_time(us_time):
    t = us_time[-2:]
    h = int(us_time[0:2])
    if t == "PM":
        if h != 12:
            h = h + 12
    elif h == 12:
        h = 0
    h = str(h)
    if len(h) < 2:
        h = "0" + h
    milTime = h + us_time[2:5]
    return milTime
print((get_military_time("07:05 PM")))
print((get_military_time("07:05 AM")))
print((get_military_time("12:05 AM")))
print((get_military_time("12:05 PM")))
