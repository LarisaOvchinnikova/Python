from datetime import datetime

def time_to_24h(time_12):
    time = datetime.strptime(time_12, "%I:%M %p")
    time_24 = time.strftime("%H:%M")
    return time_24

def time_to_12h(time_24):
    time = datetime.strptime(time_24, "%H:%M")
    time_12= time.strftime("%I:%M %p")
    return time_12

print(time_to_24h("1:30 PM"))
print(time_to_24h("12:30 AM"))

print(time_to_12h("14:30"))
print(time_to_12h("11:30"))