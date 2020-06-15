def us_time(time):
    time = time.split(":")
    h = int(time[0])
    m = time[1]

    if h == 12:
        return f"{12}:{m} PM"
    elif h == 0:
        return f"{12}:{m} AM"
    elif h < 12:
        return f"{h}:{m} AM"
    else:
        h = h - 12
        return f"{h}:{m} PM"


print(us_time("12:05"))
print(us_time("00:05"))
print(us_time("01:05"))
print(us_time("17:05"))