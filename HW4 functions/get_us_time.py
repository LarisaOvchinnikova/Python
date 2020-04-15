def get_us_time(mil_time):
    h = int(mil_time[0:2])
    if h >= 0 and h <= 11:
        h = h
        time = 'AM'
    elif h == 12:
        h = h
        time = 'PM'
    elif h >= 13 and h <= 23:
        h = h - 12
        time = 'PM'
    elif h == 24:
        h = 0
        time = 'AM'
    h = str(h)
    if len(h) < 2:
        h = '0' + h
    return h + mil_time[2:5] + ' ' + time
print(get_us_time("17:01"))
print(get_us_time("01:01"))
print(get_us_time("11:01"))
print(get_us_time("12:01"))
print(get_us_time("13:01"))
print(get_us_time("23:01"))
print(get_us_time("23:59"))
print(get_us_time("00:00"))
