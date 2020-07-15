from datetime import datetime

def time_to_24h(time_12):
    time = datetime.strptime(time_12, "%I:%M %p")
    time_24 = time.strftime("%H:%M")
    return time_24

print(time_to_24h("1:30 PM"))
print(time_to_24h("12:30 AM"))